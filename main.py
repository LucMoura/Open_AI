from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            #se quiser mudar o prompt, mude aqui no content
            "role": "system",
            "content": "fale como um aluno do nono ano do ensino medio"#<-- Mude este texto
        },
        {
            #se quiser mudar a pergunta, mude aqui no content
            "role" : "user",
            "content" : "qual é a formula do teorema de pitagoras?"#<-- Mude este texto
        }
        
    ],
    model="gpt-3.5-turbo"
)

print(resposta.choices[0].message.content)