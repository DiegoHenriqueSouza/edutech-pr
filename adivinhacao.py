import random

def jogar():

    print("***********************************")
    print("bem vindo no jogo de adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("qual o nivel de dificuldade:")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o Nível:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou" , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100!")
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(chute_maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto")
            if(chute_menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("O número secreto era", numero_secreto)
    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()