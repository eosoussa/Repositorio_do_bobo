import requests

#Isso seria para pegar, por isto usamos o get
resposta = requests.get("https://restcountries.com/v3.1/currency/real")

#Status code seria para mostrar se não tem algum errro (200 = OK) (404 = ERRO) (400 = Não encontrado)
print("Código de Status", resposta.status_code)
#Headers seria para mostrar o que está tendo no requests
print("Cabeçalhos (headers):", resposta.headers)
dicionario_reposta = resposta.json()
#print("Corpo (body)", resposta.jason())

print(dicionario_reposta[0]["name"]["official"])