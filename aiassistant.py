import openai, os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

def ask_ai():
    try:
        prompt = input("What would you like to ask me? ")
        response = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        answer = (response.choices[0].message.content or "").strip()
        print(answer)
    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        print("I'm sorry, but I'm currently unable to process that request.")