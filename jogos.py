import forca
import adivinhacao

print("Selecione um jogo:")
print("1- Adivinhação 2- Forca")
jogo = int(input("Digite o número do jogo: "))
if(jogo == 1):
    print("Jogo de adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogo de forca")
    forca.jogar()
 