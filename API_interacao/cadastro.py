import requests

nome = input("Digite o nome que deseja cadastrar: ")
email = input("Digite o e-mail que deseja cadastrar: ") 
idade = int(input("Digite a idade da pessoa: "))

corpo = {
    "nome":nome,
    "email":email,
    "idade":idade
        }

resposta = requests.post("https://172.25.129;160:5000/clientes", json=corpo)

print("Status da Resposta:",resposta.status_code)
print("Corpo da resposta:",resposta.json())