# Usage guide

This repository provides examples for using **Ollama** and **OpenAI** with Python.

## 📂 Examples

* `1_basic.py` → Basic Ollama example (text only)
* `2_images.py` → Image interpretation with Ollama
* `3_safecall.py` → Image interpretation with Ollama (fail safe mode)
* `4_loopthroughimages.py` → Images interpretation with Ollama (looping through images in a folder)
* `5_openai.py` → Image interpretation with OpenAI (fail safe mode)

---

## 🚀 OLLAMA

1. Download Ollama from [ollama.com](https://ollama.com).
2. **Recommended**: activate plane mode in Ollama if you are working with sensitive information.
3. Open a terminal and run:
   ```bash
   ollama pull XXXX

* `XXXX` is the model and version you want from [ollama.com/library](https://ollama.com/library).
* **Recommended**: run
  ```bash
  ollama list
  ```
  and store the ID of the model you downloaded (you might need to report this, later on).

4. Install the Python library:
   ```bash
   pip install ollama
   ```
5. Try running the examples:
   ```bash
   python 1_basic.py
   ```

---

## 🔑 OPENAI

1. Get an OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
2. Install the Python packages:

   ```bash
   pip install openai
   pip install pillow
   ```
3. Run an example:
   ```bash
   python 5_openai.py
   ```
