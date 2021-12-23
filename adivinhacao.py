import random

def jogar():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("! Bem vindo ao jogo de adivinhação !")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    dificuldade = 0 
    numMinimo = 0
    numMaximo = 0
    tentativasTotal = 0

    while(dificuldade == 0):
        dificuldade = int(input("Digite o nível de dificuldade entre 1-3: "))
        if(dificuldade == 1):
            numMinimo = 1
            numMaximo = 25
            tentativasTotal = 5
        elif(dificuldade == 2):
            numMinimo = 1
            numMaximo = 50
            tentativasTotal = 10
        elif(dificuldade == 3):
            numMinimo = 1
            numMaximo = 100
            tentativasTotal = 15
        else:
            print("Opção inválida")
            dificuldade = 0


    numeroSecreto = round(random.randrange(numMinimo, numMaximo + 1))


    for rodadaAtual in range(1, tentativasTotal + 1):

        print("Rodada {} de {}".format(rodadaAtual, tentativasTotal))

        numero = int(input("Digite o número entre {} e {}: ".format(numMinimo, numMaximo)))

        if(numero < numMinimo or numero > numMaximo):
            print("Você deve digitar um número entre {} e {}".format(numMinimo, numMaximo))
            continue

        acertou = numero == numeroSecreto
        maior   = numero > numeroSecreto
        menor   = numero < numeroSecreto


        if(acertou):
            print("Você acertou!")
            break
        else:
            if(maior):
                print("Quase! um pouco mais baixo...")
            elif(menor):
                print("Quase! um pouco mais alto...")

    k = input("Fim do jogo, o número era {}, aperte enter para sair.".format(numeroSecreto))

if(__name__ == "__main__"):
    jogar()