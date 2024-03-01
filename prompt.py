import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    API_KEY = os.environ.get("OPENAI_API_KEY")

    if API_KEY is None:
        raise ValueError("API_KEY is not set. Please set it in a .env file.")

    client = OpenAI(
        # This is the default and can be omitted
        api_key=API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )

    print(chat_completion["choices"][0]["message"]["content"])