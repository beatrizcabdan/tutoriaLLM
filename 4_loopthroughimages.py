from LLMcalls import chat_ollama
import os

model = "llama3.2-vision"
prompt = "Is the driver attentive?"

images = ["images/" + f for f in os.listdir("images/") if os.path.isfile(os.path.join("images/", f))]

if __name__ == '__main__':
	for image in images:
		response = chat_ollama(model, prompt, image)
		print(image)
		print(response['message']['content'])
