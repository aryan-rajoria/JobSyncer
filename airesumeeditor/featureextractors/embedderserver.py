# Embedder server app here
# this also contains the queue used for this module

import json
from typing import List
from flask import Flask, request, jsonify
from ray.util.queue import Queue
from featureextractor import SentenceEmbedder
from embedder_queue import sentencetransformer_respond, start_llm_backend, queue_backend_embedder, is_all_queue_full
import ray

"""
sample output of embedding
embedding = {
    "projects": {
        "proj1": [embeddings, [list_feature_embeddings]]
        "proj2": [embeddings,[list_feature_embeddings]]....
    }
    "
}
"""
embeddings = {}

app = Flask(__name__)
queue_list = start_llm_backend(max_con=4)

@app.route('/cv', methods=['POST'])
def embeddings():
    if request.method == 'POST':
        data = request.get_json()

        # Basic input validation (expand as needed)
        if not data or isinstance(data, List):
            return jsonify({"error": "Invalid input data"}), 400

        # Check queue availability (optional for better error handling)
        if is_all_queue_full(queue_list):
            return jsonify({"error": "All queues are full, please try again later"}), 503

        response = "Added"
        if response is None:
            # Robust error handling (e.g., model error, retry logic, etc.)
            return jsonify({"error": "Internal server error"}), 500

        return jsonify({"choices": [{"message": {"content": response}}]})


@app.route('/jd', methods=['POST'])
def embeddingsjd():
    if request.method == 'POST':
        data = request.get_json()

        # Basic input validation (expand as needed)
        if not data or "conversation" not in data:
            return jsonify({"error": "Invalid input data"}), 400

        # Check queue availability (optional for better error handling)
        if is_all_queue_full(queue_list):
            return jsonify({"error": "All queues are full, please try again later"}), 503

        response = queue_backend_embedder(data["conversation"], queue_list)
        if response is None:
            # Robust error handling (e.g., model error, retry logic, etc.)
            return jsonify({"error": "Internal server error"}), 500

        return jsonify({"choices": [{"message": {"content": response}}]})


if __name__ == '__main__':
    app.run(debug=True, port=9001)