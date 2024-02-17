from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "fale como um aluno do nono ano do ensino medio"
        },
        {
            "role" : "user",
            "content" : "qual é a formula do teorema de pitagoras?"
        }
        
    ],
    model="gpt-3.5-turbo"
)

print(resposta.choices[0].message.content)