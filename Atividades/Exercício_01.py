# Faça um programa que calcule a média de três números inseridos pelo usuário.

def calcular_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print("A média calculada é: ", calcular_media(num1, num2, num3))


# Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

num = int(input("Digite um número: "))
resultado = par_ou_impar(num)
print(f"O número {num} é {resultado}.")


# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

def imprimir_pares(numero):
    for i in range(0, numero + 1, 2):
        print(i)

num = int(input("Digite um número: "))
print(f"Números pares de 0 até {num}:")
imprimir_pares(num)


# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

def maior_menor(lista):
    maior = menor = lista[0]
    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return maior, menor

numeros = input("Digite uma lista de números (separados por espaços): ").split()
numeros = [float(numero) for numero in numeros]

maior_valor, menor_valor = maior_menor(numeros)
print(f"O maior valor na lista é: {maior_valor}")
print(f"O menor valor na lista é: {menor_valor}")


# Faça um programa que leia uma lista de números e retorne a média dos números pares.

def calcular_media_pares(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]

    if not numeros_pares:
        return 0

    media = sum(numeros_pares) / len(numeros_pares)
    return media

numeros = []
while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    numero = float(entrada)
    numeros.append(numero)

media_pares = calcular_media_pares(numeros)
if media_pares == 0:
    print("Não foram encontrados números pares na lista.")
else:
    print(f"A média dos números pares é: {media_pares:.2f}")


# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

num = int(input("Digite um número inteiro positivo: "))
if num < 0:
    print("O número deve ser positivo.")
else:
    resultado = calcular_fatorial(num)
    print(f"O fatorial de {num} é: {resultado}")


# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

def fibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))
sequencia_fibonacci = fibonacci(limite)

print("Sequência de Fibonacci até", limite)
for num in sequencia_fibonacci:
    print(num, end=" ")


# Faça um programa que determine se um número é primo ou não.

def verificar_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Digite um número: "))
if verificar_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")


# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

def nomes_comeca_com_a(lista_nomes):
    nomes_comecando_com_a = [nome for nome in lista_nomes if nome.startswith('A') or nome.startswith('a')]
    return nomes_comecando_com_a

num_nomes = int(input("Digite a quantidade de nomes na lista: "))
nomes = []

for i in range(num_nomes):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

print("Nomes que começam com 'A':", nomes_comeca_com_a(nomes))


# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.

import random

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or (escolha_usuario == "tesoura" and escolha_computador == "papel") or (escolha_usuario == "papel" and escolha_computador == "pedra"):
        return "Você venceu!"
    else:
        return "O computador venceu."

def jogar_novamente():
    return input("Deseja jogar novamente? (s/n): ").lower() == 's'

opcoes = ["pedra", "papel", "tesoura"]

while True:
    escolha_usuario = input("Escolha: pedra, papel ou tesoura: ").lower()
    
    if escolha_usuario in opcoes:
        escolha_computador = random.choice(opcoes)
        print(f"Computador escolheu: {escolha_computador}")
        resultado = determinar_vencedor(escolha_usuario, escolha_computador)
        print(resultado)
    else:
        print("Escolha inválida. Escolha entre pedra, papel ou tesoura.")

    if not jogar_novamente():
        break

