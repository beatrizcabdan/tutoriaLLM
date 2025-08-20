from LLMcalls import chat_ollama

if __name__ == '__main__':
	model = "llama3.2-vision"
	prompt = "Is the driver attentive?"
	image = "images/frame_0006.png"

	response = chat_ollama(model, prompt, image)
	print(response['message']['content'])
