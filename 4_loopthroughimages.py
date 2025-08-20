from ollamacalls import safe_chat
import os

model = "llava"
prompt = "Is the driver attentive?"

images = ["images/" + f for f in os.listdir("images/") if os.path.isfile(os.path.join("images/", f))]

if __name__ == '__main__':
	for image in images:
		response = safe_chat(model, prompt, image)
		print(image)
		print(response['message']['content'])
