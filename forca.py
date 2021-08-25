import random


def jogar():
    print("**********************************")
    print("***bem vindo no jogo de forca****!")
    print("**********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)


    arquivo.close()


    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):

        print("Voce tem", erros, "chances")
        print("")
        print("Dica : Fruta")
        chute = input("Qual a letra ? ")
        print("")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            print("A letra", chute, "não existe no jogo")
            print("")
            erros = erros - 1

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)



    if(acertou):
        print("Voce Ganhou !!!!")
    else:
        print("Voce Perdeu !!!!")

    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()