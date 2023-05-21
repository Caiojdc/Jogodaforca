import random
import os as os
import time

# Variáveis       
# teste git                
# Adicionar ou Remover palavras Aqui \|/
palavras = ["computador", "cachorro", "mulher", "brasil", "parede"]

tentativas = 0
chances = 6
letrasEscolhidas=[]
palavra = random.choice(palavras)
estadoAtual = [" __ "] * len(palavra)

# Imprimindo o Boneco

def imprimeForca(chances):
    if chances == 6:
        print("   _____ ")
        print("  |      ")
        print("  |      ")
        print("  |      ")
        print("  |      ")
    elif chances == 5:
        print("   _____ ")
        print("  |    O ")
        print("  |      ")
        print("  |      ")
        print("  |      ")
    elif chances == 4:
        print("   _____ ")
        print("  |    O ")
        print("  |    | ")
        print("  |      ")
        print("  |      ")
    elif chances == 3:
        print("   _____ ")
        print("  |    O ")
        print("  |   /| ")
        print("  |      ")
        print("  |      ")
    elif chances == 2:
        print("   _____ ")
        print("  |    O ")
        print("  |   /|\\")
        print("  |      ")
        print("  |      ")
    elif chances == 1:
        print("   _____ ")
        print("  |    O ")
        print("  |   /|\\")
        print("  |   /  ")
        print("  |      ")
    elif chances == 0:
        print("   _____ ")
        print("  |    O ")
        print("  |   /|\\")
        print("  |   / \\")
        print("  |       ")

# Tela de Início

def inicio():
    print('     SEJA BEM VINDO AO')
    print('           JOGO')
    print('            DA')
    print('          FORCA')



def main():
    global palavras
    global tentativas
    global chances
    global letrasEscolhidas
    global palavra
    global estadoAtual

    inicio()
    input("Pressione <enter> para continuar")

    while tentativas < chances and ''.join(estadoAtual) != palavra:
        
        os.system('cls')

        imprimeForca(chances)        

        print("\n")

        print("Letras Escolhidas:","\t\t Tentativas Restante:", chances)
        for i in letrasEscolhidas:
            print(i, end=' ')

        print("\n")

        for i in estadoAtual:
            print(i, end=' ')

        letra = input("\n\n Qual letra vc quer arriscar? ")
                
        while letra in letrasEscolhidas:
            print("Você escolheu uma letra que já tinha tentado, escolha outra")
            letra = input("Qual outra letra você quer tentar? ")

        letrasEscolhidas.append(letra)
        
        if letra in palavra:
            print("Parabéns, você acertou a letra!")
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    estadoAtual[i] = letra
        else:
            print("Que pena, você errou!")
            chances = chances - 1
            

        time.sleep(1.0)
        
    # Resultado
        
    if tentativas == chances:
        os.system('cls')
        print("você foi enforcado x_x")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print(" /                   \  ")
        print(" |   XXXX     XXXX   |  ")
        print(" |   XXXX     XXXX   |    ")
        print(" |   XXX       XXX   |         A PALAVRA ERA:",palavra)
        print(" |                   |              "  )
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        input("")
    else:
        os.system('cls')
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     A PALAVRA ERA:",palavra)
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        input('')

if __name__ == '__main__':
    main()