import os, openai
from dotenv import load_dotenv

load_dotenv()

# ? OpenAI ChatGPT Docs => https://platform.openai.com/docs/api-reference/chat/create
# ? Lib https://platform.openai.com/docs/libraries

def message_gpt():
    # TODO: Should happen in main.py
    openai.api_key = os.getenv("AUTHORIZATION")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            "Hello, ChagtGPT! 🤓"
        ]
    )

    return response

print(message_gpt())