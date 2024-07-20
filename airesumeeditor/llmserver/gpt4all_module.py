from gpt4all import GPT4All
import ray

@ray.remote(num_cpus=6)
def gpt4all_respond(queue_list):
    gpt4all_model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    gpt4all_model.model.set_thread_count(6)

    # Remote processing to detach from client process.
    while True:
        for iq, oq in queue_list:
            if iq.empty():
                continue

            conversation = iq.get()
            system_template = conversation[0]["content"]
            document = conversation[1]["content"]
            query = conversation[2]["content"]
            user_template = "Document:{0}\nThe question is:{1}\nAnswer:".format(
                document, query
            )
            
            response = ""
            with gpt4all_model.chat_session():
                print(system_template + user_template)
                response = gpt4all_model.generate(query + system_template + "\n" + user_template, temp=0, repeat_penalty=1.4)
            oq.put(response)

def start_llm_backend(max_con=1):
    ray.init()
    from ray.util.queue import Queue

    # Concurrent queue to interact with backend GPT4ALL inference.
    queue_list = [(Queue(maxsize=1), Queue(maxsize=1)) for _ in range(max_con)]
    gpt4all_respond.remote(queue_list)
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

class LLMGPT4All:

    def __init__(self, model_name=None):
        self.model = model_name
        if self.model is not None:
            self.load_model(self.model)

    def load_model(self, model_name):
        self.model = GPT4All(model_name)
    
    def generate_answer(self, question, max_token=1024):
        with self.model.chat_session():
            return self.model.generate(question, max_token=max_token)