import ollama

class SmartAgent:
    def __init__(self, model):
        self.model_name = model
        self.chat_log = []

    def chat(self, message):
        self.chat_log.append({'role': 'user', 'content': message})
        answer = ollama.chat(
            model=self.model_name,
            messages=self.chat_log)
        answer_text = answer['message']['content']
        self.chat_log.append({'role': 'agent', 'content': answer_text})
        return answer_text