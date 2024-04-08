"""Elabore um programa de implemente umjogo de Craps, conforme descrição a seguir: 
O jogador lança um par de dados (2 números aleatórios entre 1 e 6), obtendo um valor entre
2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você tirou um "natural" e ganhou. Se você
tirar 2, 3 ou 12 na primeira jogada, isto échamado de "Craps" e você perdeu. Se, na 
primeira jogada, você fizer um 4, 5, 6, 8, 9 ou 10, este é o seu "Ponto". Seu objetivo agora é
continuar jogando os dados até tirar este número novamente. Você perde, no entanto, 
se tirar um 7 antes de tirar este "Ponto" novamente"""

#Jogo CRAPS solicitar nome e valor apostado no inicio do jogo. Salvar nome, valor, resultado em arquivo txt
    # Ao finalizar o jogo listar as apostas em 2 grupos => Ganhadores e Perdedores 
import random
import time

num_jogadas = 0
soma_dados = 0
while True:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(f"Você jogos os dados e os números foram:{dado1} e {dado2}")
    time.sleep(2)
    soma_dados = dado1+dado2
    if num_jogadas== 0 and soma_dados == 7 or soma_dados == 11:
        print(f"Parabéns, tirou um NATURAL, você venceu! 🏆🏆")
        break
    elif num_jogadas== 0 and soma_dados == 2 or soma_dados== 3 or soma_dados == 12:
        print(f"Que azar, você tirou um CRAPS, você perdeu!!😢😢")
        break
    else:
        while True:
            time.sleep(1)
            print(f"Você marcou PONTO com o valor de {soma_dados}, você deve tirar o mesmo número para vencer!")
            time.sleep(1)
            num_jogadas +=1
            dado01 = random.randint(1,6)
            dado02 = random.randint(1,6)
            soma_dados2 = dado1 + dado02
            if soma_dados == soma_dados2:
              print(f"Parabéns, tirou seu objetivo PONTO seus dados iguais foram {soma_dados2}, você venceu! 🏆🏆")
              time.sleep(1)
              break
            elif soma_dados2 == 7:
              print(f"Que azar, você tirou um 7, você perdeu!!😢😢")
              time.sleep(1)
              break
            else:
              print(f"Soma dos dados foram,{soma_dados2}. Diferente dos números da sua jogada PONTO")
              soma_dados2 = 0
              time.sleep(1)
              continua = input("Deseja outra carta(S/N): ").upper()
              if continua == "N":
                break
    break      
        
                  
      


