import ollama

# Specify the model name
model_name = "llama3.2"

# Define the prompt
prompt = "What is the capital of France?"

# Send the prompt to the model and get the response
answer = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])

# Print the response
print(type(answer))
answer_text = answer['message']['content']
print(answer_text)