# Setup Guide

This repository provides examples for using **Ollama** and **OpenAI** with Python.

## 📂 Example Files

* `1_basic.py` → Basic Ollama example (text only)
* `2_images.py` → Image interpretation with Ollama
* Etc.

---

## 🚀 OLLAMA

1. Download Ollama from [ollama.com](https://ollama.com).
2. **Recommended**: activate **plane mode** in Ollama if you are working with sensitive information.
3. Open a terminal and run:
   ```bash
   ollama pull XXXX

* `XXXX` is the model and version you want from [ollama.com/library](https://ollama.com/library).
* **Recommended**: run
  ```bash
  ollama list
  ```
  and store the **ID** of the model you downloaded (you might need to report this, later on).

4. Install the Python library:
   ```bash
   pip install ollama
   ```
5. Try running the examples:
   ```python 1_basic.py
   ```

---

## 🔑 OPENAI

0. Get an OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
1. Install the Python packages:

   ```bash
   pip install openai
   pip install pillow
   ```
2. Run the example:
   ```bash
   python 5_openai.py
   ```
