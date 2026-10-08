from model import load_model
from chat import generate_response
from memory import remember


def main():

    print("=" * 40)
    print("              LLM")
    print("=" * 40)

    print("\nLoading model...\n")

    model = load_model()

    print("\nLLM is ready!")
    print("Type 'exit' to stop.")
    print("Use /remember key=value to save something.\n")

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

        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("\nChat ended.")
            break

        if user_input.startswith("/remember "):

            data = user_input[len("/remember "):]

            if "=" not in data:
                print("Use: /remember key=value\n")
                continue

            key, value = data.split("=", 1)

            key = key.strip()
            value = value.strip()

            if key and value:
                remember(key, value)
                print(f"Memory saved: {key} = {value}\n")
            else:
                print("Both key and value are required.\n")

            continue

        response = generate_response(
            user_input,
            model,
            conversation
        )

        print("LLM:", response)
        print()


if __name__ == "__main__":
    main()