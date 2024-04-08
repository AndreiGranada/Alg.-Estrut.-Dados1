import os

compras = []
precos = []

def titulo(texto, sublinhado="="):
    print()
    print(texto)
    print (sublinhado*40)

def incluir():
    titulo("Inclusão de Compras", "-")
    compra = input("Descrição da compra: ")
    preco = float(input("Valor Previsto R$: "))
    compras.append(compra)
    precos.append(preco)
    print("Ok. Compra cadastrada com sucesso")
def listar():
    titulo("Compras Cadastradas", "-")
    print("Descrição da Compra ...............: R$ Previsto:")
    print("-------------------------------------------------")
    for compra , preco in zip(compras, precos):
        print(f"{compra:30s} {preco:12.2f}")
def grava_compras():
    with open("compras.txt", "w") as arq:
        for compra, preco in zip(compras , precos):
            arq.write(f"{compra}; {preco}/n")

def carrega_compras():
    if not os.path.isfile("compras.txt"):
        return
    with open("compras.txt", "r") as arq:
        dados = arq.readlines()
        for linha in dados:
            partes = linha.split(";")
            compras.append(partes[0])
            precos.append(float(partes[1]))

def listar_ordem():
    pass


def excluir():
    pass




carrega_compras()
while True:
    titulo("Lista de compras da semana")
    print("1.Incluir Compra")
    print("2.Listar compras")
    print("3.Lista de compras em ordem")
    print("4.Excluir Compra")
    print("5.Finalizar")
    opcao = int(input("Opção: "))
    if opcao ==1:
        incluir()
    elif opcao ==2:
        listar()
    elif opcao ==3:
        listar_ordem()
    elif opcao ==4:
        excluir()
    else:
        grava_compras()
        break    

    #Exercícios 
    # 1Concluir as funções => listar compras em ordem ; Excluir Compra; Na listagem totalizar o valor
    #mudança no arquivo02