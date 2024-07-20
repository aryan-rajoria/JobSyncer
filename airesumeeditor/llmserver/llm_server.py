# flask app here
import json
from flask import Flask, request, jsonify
from ray.util.queue import Queue

from gpt4all_module import (
    start_llm_backend,
    queue_backend_llm,
    is_all_queue_full,
)  # Import functions from your LLM backend

app = Flask(__name__)
queue_list = start_llm_backend(max_con=2)  # Adjust max_con based on resources

@app.route('/chat', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True, port=9003)