import ollama

from config import MODEL_ID


def load_model():

    print("Connecting to Ollama...")

    ollama.show(MODEL_ID)

    print("Mistral 7B loaded successfully.")

    return MODEL_ID