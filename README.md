# README

## Description

The purpose of this repository was to experiment with local LLMs using Ollama.
We created a python script that sends the same prompt to two different models and saves their responses in a CSV-file.

**Models used:**

- `Qwen3:4b`
- `Gemma3:4b`

---

## 🚀 How To Run

1. Python installed
2. Ollama installed and running
3. Qwen3:4b and Gemma 3:4b downloaded through Ollama
4. Run the script in your IDE terminal:
   `python .\10_call_models.py`

The script sends the same prompt to both models one at a time, and saves the responses in `results.csv`

---

## Our observations

Both models were pretty slow generating responses. We occasionally experienced timeouts, especially with Qwen3:4b.

The order in which the models were executed seemed to affect the performance. Running a model requires a huge amount of RAM, running one model first seems to affect the available memory the the second model.

The responses was much less accurate than those from larger commerical language models like OpenAIs GPT models or Anthropics Claude models.

Both models was able to answer simple questions correctly, like "what is the capital of Sweden" or common riddles. However they sometimes hallucinated answers. For example, Gemma 3:4b answered "This is a classic riddle The answer is a table" to the trick question "What has two legs but cannot drive a motorcycle?". The models also tended to give really long answers even to simple questions.

To summarize, the models performed OK on simple questions but was not reliable when handling unusual prompts.
