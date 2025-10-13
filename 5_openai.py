from openai import OpenAI
from LLMcalls import chat_openai_image

if __name__ == '__main__':
    key = open("openai_key.txt", 'r').read()
    openai = OpenAI(api_key=key)

    model = "gpt-4o"
    prompt = "Is the driver attentive?"
    image = "images/frame1.png"

    response = chat_openai_image(openai, model, prompt, image)
    print(response)
