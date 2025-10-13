from LLMcalls import chat_ollama

if __name__ == '__main__':
	model = "llama3.2"
	prompt = "What is the capital of Sweden?"
	response = chat_ollama(model, prompt)
	print(response['message']['content'])

	model = "llama3.2-vision"
	prompt = "Is the driver attentive?"
	image = "images/frame1.png"
	response = chat_ollama(model, prompt, image)
	print(response['message']['content'])
