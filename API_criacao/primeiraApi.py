#Importando somente Flask do pacote flask
from flask import Flask
#criar a minha aplicação Flask
app = Flask(__name__)
#Criando a rota '/'
#A rota chama uma função
@app.route('/')
def ola():
    return "Olá, Flask!"
#Agora precisamos rodar essa aplicação
app.run()