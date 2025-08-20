import ollama

model = "llama3.2"
prompt = "What is the capital of Sweden?"

response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
print(response['message']['content'])
