import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client=genai.Client(api_key=os.getenv("API_KEY"))

def sulp(a:float,b:float)->float:
    """Dodaje a od b"""
    return a+b

def ffid(a:float,b:float)->float:
    """Odejmuje b od a"""
    return a-b

tools=[sulp,ffid]

chat=client.chats.create(
    model="gemini-2.5-flash",
    config=genai.types.GenerateContentConfig(
        tools=tools,
        temperature=0.0,  
        system_instruction="Jesteś pomocnym asystentem matematycznym. Zawsze używaj dostarczonych narzędzi do obliczeń."
    )
)
pytanie="Ile to jest 145 plus 87, a potem odejmij od tego 32?"
response=chat.send_message(pytanie)
print(f"Odpowiedź na twoje pytanko to: {response.text}")
