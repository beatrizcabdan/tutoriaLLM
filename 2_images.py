import ollama

model = "llama3.2-vision"
prompt = "Is the driver attentive?"
image = "images/frame_0006.png"

response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt, "images": [image]}])
print(response['message']['content'])
