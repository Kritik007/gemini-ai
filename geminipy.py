import textwrap

import google.generativeai as genai

from IPython.display import Markdown
import os


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Fetch API key from environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    print("Error: API key not found in environment variable.")
    exit()
genai.configure(api_key=GOOGLE_API_KEY)

# Create a model
model = genai.GenerativeModel('gemini-pro')

# Chat with the model
while True:
    try:
        prompt = input('You: ')
        response = model.start_chat().send_message(prompt)
        print(f'Gemini: {response.text}')
    except KeyboardInterrupt:
        print("Keyboard Interrupt pressed...\nGemini: Exiting chat. Goodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
