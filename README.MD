
# LLM

A standalone Python LLM application using the pretrained
Mistral 7B Instruct v0.2 model through Ollama.

## Model

mistral:7b-instruct-v0.2-q4_K_M

Original model:
mistralai/Mistral-7B-Instruct-v0.2

## Features

- Real pretrained Mistral 7B model
- Local inference using Ollama
- Conversational chat
- Conversation context
- Persistent JSON memory
- Modular Python structure

## Project Structure

```text
LLM/
├── main.py
├── model.py
├── chat.py
├── memory.py
├── config.py
├── memory.json
├── requirements.txt
├── README.md
└── .gitignore
````

## Requirements

* Python 3.12+
* Ollama
* Mistral 7B Instruct v0.2
* Git

## Installation

Install the Python dependency:

```bash
pip install -r requirements.txt
```

Download the Mistral model:

```bash
ollama pull mistral:7b-instruct-v0.2-q4_K_M
```

## Run

```bash
python main.py
```

## Persistent Memory

The application stores user information in:

```text
memory.json
```

To save information during a chat:

```text
/remember key=value
```

Example:

```text
/remember favorite_language=Python
```

The saved information remains available after restarting the application.

## Model Source

Hugging Face:

mistralai/Mistral-7B-Instruct-v0.2

## Purpose

This project is built for learning and experimentation with
a real pretrained large language model running locally.

```

