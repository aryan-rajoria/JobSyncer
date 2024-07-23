# Embedder server app here
# this also contains the queue used for this module

import json
from typing import List
from flask import Flask, request, jsonify
from ray.util.queue import Queue
from featureextractor import SentenceEmbedder
from embedderhandler import EmbedCV, JDEmbed, SegmentsHandler
from embedder_queue import sentencetransformer_respond, start_llm_backend, queue_backend_embedder, is_all_queue_full
import ray

"""
sample output of embedding
embedding = {
    "projects": {
        "proj1": [embeddings,[list_feature_embeddings]]
        "proj2": [embeddings,[list_feature_embeddings]]....
    }
    "
}
"""

app = Flask(__name__)
queue_list = start_llm_backend(max_con=1)
embed_handler = EmbedCV(queue_list)
jd_embed = JDEmbed()

@app.route('/cv', methods=['POST'])
def embeddings():
    if request.method == 'POST':
        data = request.get_json()

        # Basic input validation (expand as needed)
        if not (isinstance(data, list) and len(data)>0):
            return jsonify({"error": "Invalid input data"}), 400

        # Check queue availability (optional for better error handling)
        if is_all_queue_full(queue_list):
            return jsonify({"error": "All queues are full, please try again later"}), 503

        if embed_handler.embed_all(data):
            response = "Added"
        else:
            resonse = "some error"
        if response is None:
            # Robust error handling (e.g., model error, retry logic, etc.)
            return jsonify({"error": "Internal server error"}), 500

        return jsonify({"choices": [{"message": {"content": response}}]})


@app.route('/jd', methods=['POST'])
def embeddingsjd():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)

        # Basic input validation (expand as needed)
        if not (isinstance(data, dict) and len(data)>0):
            return jsonify({"error": "Invalid input data"}), 400

        # Check queue availability (optional for better error handling)
        if is_all_queue_full(queue_list):
            return jsonify({"error": "All queues are full, please try again later"}), 503

        response = queue_backend_embedder(data["jd"], queue_list)
        jd_embed.jd_embed = response
        if response is None:
            # Robust error handling (e.g., model error, retry logic, etc.)
            return jsonify({"error": "Internal server error"}), 500

        return jsonify({"choices": [{"message": {"content": "Add done"}}]})

@app.route('/resume_layout', methods=['GET'])
def layout():
    if not embed_handler.embeddings or(jd_embed.jd_embed.size==0):
        return jsonify({"error": "Improper access"}, 412)
    
    segments = SegmentsHandler(embed_handler, jd_embed.jd_embed, 0.1)
    layout = segments.optimize_layout()

    return jsonify({"wow": "wow"}, 500)


if __name__ == '__main__':
    app.run(debug=True, port=9001)