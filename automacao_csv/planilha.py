import csv
#abrindo o arquivo csv com função open e chamando de planilha
with open("Automacao_csv/example3.CSV") as planilha:              # O for percorre a lista 
    #Lendo os dados csv usando o 'reader'(leitor)
    leitorCSV = csv.reader(planilha)
    #Convertendo esses dados para uma lista python
    planilha_python = (list(leitorCSV))
    total = 0
    for linha in planilha_python:
        try:
            total = total + float(linha[2])
        except:
            continue
    print("Total de vendas:",total)
    print("Média das vendas:", total/(len(planilha_python) - 1))    
