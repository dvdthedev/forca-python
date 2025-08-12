import random

palavras = []

def ler_score():
    with open('scores.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)
        arquivo.close()


def salva_score(score):
    with open('scores.txt', 'a') as arquivo:
        arquivo.write(f'{score}\n')
        arquivo.close()

with open('file.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

def palavra_random ():
    return random.choice(palavras)

opcao = 1

print('Bem vindo ao jogo da forca')


def valida_int(valor, min, max):
    try:
        x = int(input(valor))
        while x < min and x > max:
            x = int(input(valor))
        return x
    except ValueError:
        print('Você não digitou um número')

def criar_array_do_palavra(palavra):
    array = []
    for letras in palavra:
        array.append('-')
    return array


while opcao != 3:

    opcao =  valida_int('Selecione uma opção:  1- Jogar 2- Score 3- Sair ', 1 ,3)
    if opcao == 3:
        break
    elif opcao == 1:
        print('Bem vindo ao jogo da forca')
        nome = input('Digite seu nome: ')
        vidas = 5
        palavra = palavra_random()
        array = criar_array_do_palavra(palavra)
        score = 0

        while vidas > 0:
            letra = input('Digite uma letra: ').lower()
            if letra in array:
                print('Você já digitou está letra')
            elif letra not in palavra:
                vidas -= 1
                score -= 100
                print(f'Vidas: {vidas}')
                print(f'A letra {letra} não está na palavra: {array} score: {score}')
            elif letra in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        array[i] = letra
                        score += 100
                print(f'{array} score: {score}')
                if "".join(array) == palavra:
                    print(f'Você venceu! score: {score}')
                    salva_score(f'{nome}: {score}')
                    break

            if vidas == 0:
                print('Você perdeu')
    elif opcao == 2:
        ler_score()


    elif opcao == 2:
        print('Bem vindo ao jogo da forca')