from smart_agent import SmartAgent
# Specify the model name
model_name = "lemma3.1"

smart_agent = SmartAgent("lemma3.1")

question = input("question?> ").strip()
while question != "/pa":
    if question != "" :
        answer_text = smart_agent.chat(question)
        print(answer_text)
    question = input("question?> ").strip()
