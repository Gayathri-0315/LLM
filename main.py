from model import load_model
from chat import generate_response


def main():

    print("=" * 40)
    print("              LLM")
    print("=" * 40)

    print("\nLoading model...\n")

    tokenizer, model = load_model()

    print("\nLLM is ready!")
    print("Type 'exit' to stop.\n")

    conversation = [
        {
            "role": "system",
            "content": """You are a helpful AI assistant.
The user's name is Gayathri.
Never call the user Sir.
Be friendly, helpful and respectful.
Do not invent personal information.
Answer clearly and naturally."""
        }
    ]

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nChat ended.")
            break

        response = generate_response(
            user_input,
            tokenizer,
            model,
            conversation
        )

        print("LLM:", response)
        print()


if __name__ == "__main__":
    main()