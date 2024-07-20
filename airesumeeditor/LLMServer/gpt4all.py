from gpt4all import GPT4All

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