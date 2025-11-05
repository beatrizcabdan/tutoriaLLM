from LLMcalls import chat_openai, add_to_csv
from openai import OpenAI
import pandas as pd

key = open("openai_key.txt", 'r').read()
openai = OpenAI(api_key=key)

model = "gpt-4o"
prompt_part1 = "Hello!"
prompt_part3 = "Goodbye!"

prompts_csv = "prompts.csv"
results_csv = "results.csv"

csv = pd.read_csv(prompts_csv)
add_to_csv(results_csv, ["model", "cognitive_bias", "response"], new=True)
for row in csv:
	cognitive_bias = row[2]
	prompt_part2 = row[3]
	prompt = prompt_part1 + "\n" + prompt_part2 + "\n" + prompt_part3

	response = chat_openai(openai, model, prompt)
	add_to_csv(results_csv, [model, cognitive_bias, response])