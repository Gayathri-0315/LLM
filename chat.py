import torch

from config import (
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P,
    REPETITION_PENALTY
)


def generate_response(
    message,
    tokenizer,
    model,
    conversation
):

    conversation.append({
        "role": "user",
        "content": message
    })

    inputs = tokenizer.apply_chat_template(
        conversation,
        return_tensors="pt",
        add_generation_prompt=True
    )

    inputs = {
        key: value.to(model.device)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            do_sample=True,
            repetition_penalty=REPETITION_PENALTY,
            pad_token_id=tokenizer.eos_token_id
        )

    input_length = inputs["input_ids"].shape[1]

    response = tokenizer.decode(
        outputs[0][input_length:],
        skip_special_tokens=True
    ).strip()

    conversation.append({
        "role": "assistant",
        "content": response
    })

    return response