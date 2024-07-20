# Embedder server app here
# this also contains the queue used for this module

import json
from flask import Flask, request, jsonify
from ray.util.queue import Queue
from featureextractor import SentenceTransformer
import ray

@ray.remote(num_cpus=3)
def sentencetransformer_respond(text):
        model = SentenceTransformer()
        embedding = model.encode(input)
        return embedding

def start_llm_backend(max_con=1):
    ray.init()
    from ray.util.queue import Queue

    # Concurrent queue to interact with backend GPT4ALL inference.
    queue_list = [(Queue(maxsize=1), Queue(maxsize=1)) for _ in range(max_con)]
    sentencetransformer_respond.remote(queue_list)
    # openai_respond.remote(queue_list)
    return queue_list

def queue_backend_llm(conversation, queue_list):
    for iq, oq in queue_list:
        if iq.full():
            continue
        else:
            iq.put(conversation)
            return oq.get()
    return None


def is_all_queue_full(queue_list):
    for iq, _ in queue_list:
        if not iq.full():
            return False
    return True

app = Flask(__name__)
queue_list = start_llm_backend(max_con=4)  # Adjust max_con based on resources

@app.route('/embed', methods=['POST'])
def chat_completions():
    if request.method == 'POST':
        data = request.get_json()

        # Basic input validation (expand as needed)
        if not data or "conversation" not in data:
            return jsonify({"error": "Invalid input data"}), 400

        # Check queue availability (optional for better error handling)
        if is_all_queue_full(queue_list):
            return jsonify({"error": "All queues are full, please try again later"}), 503

        response = queue_backend_llm(data["conversation"], queue_list)
        if response is None:
            # Robust error handling (e.g., model error, retry logic, etc.)
            return jsonify({"error": "Internal server error"}), 500

        return jsonify({"choices": [{"message": {"content": response}}]})