import LLMcalls
import ollama
import re

def clean_string_regex(input_string):
    """Remove all non-alphanumeric characters using regex."""
    # The pattern matches any character that is NOT a letter or number
    cleaned = re.sub(r'[^A-Za-z0-9\s]', '', input_string)
    return cleaned

if __name__ == '__main__':
    models = ["qwen3:4b", "gemma3:4b"]
    prompt = "What gets wetter the more it dries?"

    filename = "results.csv"

    LLMcalls.add_to_csv(filename, ["Prompt", "Model", "Response"], new=True)

    for model in models: 
        print(model)

        response = LLMcalls.chat_ollama(model, prompt)

        answer = response["message"]["content"]
        answer = clean_string_regex(answer)
        print(answer)
        LLMcalls.add_to_csv(filename, [prompt, model, answer])