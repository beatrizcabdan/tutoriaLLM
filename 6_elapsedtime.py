from LLMcalls import chat_ollama
import time
import numpy as np

model = "gpt-oss"
prompt = "Hello!"
reps = 10
timeout_seconds = 40

if __name__ == '__main__':
    times = []
    timeouts = 0
    print(f"Prompting {reps} times {model}: {prompt}")

    for _ in range(reps):
        start = time.perf_counter()
        response = chat_ollama(model, prompt, timeout_seconds=timeout_seconds, verbose=False)
        end = time.perf_counter()
        times += [end - start]
        if response['message']['content'] == "Timeout.":
            timeouts += 1

    print(f"Average response time: {np.mean(times):.2f}+-{np.std(times):.2f} s, {timeouts} timeouts ({timeout_seconds} s)")

