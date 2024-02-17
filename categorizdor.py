from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """
            Classifique o produto abaixo em uma das categorias:Higiene
            Pessoal, Moda ou Casa e dê uma descrição da categoria
            """
        },
        {
            "role" : "user",
            "content" : """""
            Camiseta
            """
        }
        
    ],
    model="gpt-3.5-turbo",
    temperature = 0.5,
    max_tokens=257,
    n = 3,
)

for contador in range(0,3):
    print(resposta.choices[0].message.content)