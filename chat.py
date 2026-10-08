import ollama

from config import (
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P,
    REPETITION_PENALTY
)

from memory import get_memory_context


def generate_response(
    message,
    model,
    conversation
):

    memory_context = get_memory_context()

    if memory_context:
        conversation.append({
            "role": "system",
            "content": memory_context
        })

    conversation.append({
        "role": "user",
        "content": message
    })

    response = ollama.chat(
        model=model,
        messages=conversation,
        options={
            "num_predict": MAX_NEW_TOKENS,
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "repeat_penalty": REPETITION_PENALTY
        }
    )

    answer = response["message"]["content"].strip()

    conversation.append({
        "role": "assistant",
        "content": answer
    })

    return answer