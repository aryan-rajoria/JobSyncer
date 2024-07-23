import ray
from featureextractor import SentenceEmbedder

@ray.remote(num_cpus=1)
def sentencetransformer_respond(queue_list):
        model = SentenceEmbedder()
        while True:
            for iq, oq in queue_list:
                if iq.empty():
                    continue
            text = iq.get()
            embedding = model.generate_embeddings(text)
            oq.put(embedding)

def start_llm_backend(max_con=1):
    ray.init()
    from ray.util.queue import Queue

    # Concurrent queue to interact with backend GPT4ALL inference.
    queue_list = [(Queue(maxsize=1), Queue(maxsize=1)) for _ in range(max_con)]
    sentencetransformer_respond.remote(queue_list)
    # openai_respond.remote(queue_list)
    return queue_list

def queue_backend_embedder(conversation, queue_list):
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