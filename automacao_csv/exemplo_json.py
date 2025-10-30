# lista_frutas = []

# dicionario_precos = {"":1,}
# dicionario_valores = {1:"",}

lista_filmes = {
    "Stop Motion":{
        "Incrivel Mundo de jack":16,
        "Coraline":17,
        "Paranorman":25},


    "Herói":{
        "Vingadores End Game":28,
        "Espetacular Homem-Aranha":35,
        "Homem-aranha Sem Volta Para Casa":25
    },


    "Terror":{
        "Invocação Do Mal 2":40,
        "It a Coisa Capitulo I":21,
        "Invocação Do mal 4":34
    }
}

print(lista_filmes)


# dicionario_teste = {"maçã":5, "banana":6}
###MÉTODOS PRINCIPAIS DOS DICIONARIOS ###
##1. LER COM SEGURANÇA .get(chave, default(padrão))
##- O que ele faz: devolve dicionario[chave] se exostor, senão devolve padrão

# print(dicionario_teste.get("abacaxi"))
##2. VERIFICAR SE A CHAVE EXISTE in
##-  O que faz: chave in dicionario verifica chaves (não valores)

# print("abacaxi" in dicionario_teste)
# print("maçã" in dicionario_teste)
##3. Percorrer os pares (chave, valor) .items()
# for fruta, preco in dicionario_teste.items()
#    print(f"Fruta:{fruta} Custa:R$ {preco}")

# for filmes, dados in lista_filmes:
#   print(filmes,dados)