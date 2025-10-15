from LLMcalls import chat_ollama
import utils

model = "llama3.2-vision"
prompt = "Is the driver attentive?"

images = utils.load_files_in_folder("images/")

if __name__ == '__main__':
	for image in images:
		response = chat_ollama(model, prompt, image)
		print(image)
		print(response['message']['content'])
