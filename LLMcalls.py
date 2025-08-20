import ollama
import multiprocessing
from io import BytesIO
import base64
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def chat_openai(client, model, prompt, image, timeout_seconds=40):
    with ThreadPoolExecutor(max_workers=1) as ex:
        future = ex.submit(call_openai_chat, client, model, prompt, image)
        try:
            print(f"Prompting {model} with timeout {timeout_seconds}s")
            return future.result(timeout=timeout_seconds)
        except TimeoutError:
            print(f"Timeout after {timeout_seconds} seconds.")
            return "Timeout."
        except Exception as e:
            print(f"Chat call failed: {e}")
            return "Failure."


def chat_ollama(model, prompt, image, timeout_seconds=40):
    with multiprocessing.Pool(processes=1) as pool:
        async_result = pool.apply_async(call_ollama_chat, (model, prompt, image))
        try:
            print(f"Prompting {model} with timeout {timeout_seconds}s")
            result = async_result.get(timeout=timeout_seconds)
            return result
        except multiprocessing.TimeoutError:
            print(f"Timeout after {timeout_seconds} seconds.")
            pool.terminate()
            pool.join()
            return "Timeout."
        except Exception as e:
            print(f"Chat call failed: {e}")
            pool.terminate()
            pool.join()
            return "Failure."


def call_ollama_chat(current_model, prompt, image):
    return ollama.chat(model=current_model, messages=[{'role': 'user', 'content': prompt, 'images': [image]}])


def call_openai_chat(openai, model, prompt, image):
    encoded_string = encode_image(image, 2048)
    response = openai.chat.completions.create(model=model, messages=[{"role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}", }, }, ], }], max_tokens=300, )
    return response.choices[0].message.content


# OpenAI needs to receive the images encoded in base64, this does it
def encode_image(image_path, max_image=512):
  with Image.open(image_path) as img:
    width, height = img.size
    max_dim = max(width, height)
    if max_dim > max_image:
      scale_factor = max_image / max_dim
      new_width = int(width * scale_factor)
      new_height = int(height * scale_factor)
      img = img.resize((new_width, new_height))

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str
