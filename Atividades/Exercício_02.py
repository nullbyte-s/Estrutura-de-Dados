# Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = math.pi * self.raio ** 2
        return area

raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print(f"A área do círculo é: {circulo.calcular_area():.2f}")


# Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

livro = Livro("Admirável Mundo Novo", "Aldous Huxley")
print(livro.detalhes())
livro = Livro("O Clube do Crime das Quintas-Feiras", "Richard Osman")
print(livro.detalhes())


# Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
retangulo = Retangulo(base, altura)
print(f"A área do retângulo é: {retangulo.calcular_area()}")


# Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo:.2f}")

titular = str(input("Insira o nome do titular da conta: "))
print(f"Bem-vindo(a), {titular}")
ContaBancaria(titular)

valor_deposito = float(input("Digite o valor a ser depositado: "))
conta.depositar(valor_deposito)
valor_saque = float(input("Digite o valor a ser sacado: "))
conta.sacar(valor_saque)


# Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} ({self.idade} anos) está falando... 🎤🙋‍♀️")

pessoa = Pessoa("Ana", 25)
pessoa.falar()
pessoa = Pessoa("Zelda", 22)
pessoa.falar()


# Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"

carro = Carro("Fiat", "Uno", 2013)
print(carro.detalhes())
carro = Carro("Honda", "Civic", 2016)
print(carro.detalhes())


# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        total_notas = sum(self.notas)
        media = total_notas / len(self.notas)
        return media

nome_aluno = input("Digite o nome do aluno: ")
notas_aluno = []

while True:
    entrada = input("Digite uma nota (ou 'finalizar' para encerrar): ")
    if entrada.lower() == 'finalizar':
        break
    nota = float(entrada)
    notas_aluno.append(nota)

aluno = Aluno(nome_aluno, notas_aluno)
print(f"A média das notas do aluno {aluno.nome} é: {aluno.calcular_media():.2f}")


# Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro

lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
triangulo = Triangulo(lado1, lado2, lado3)
print(f"O perímetro do triângulo é: {triangulo.calcular_perimetro()}")


# Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Salário de {self.nome} aumentado para R${self.salario:.2f}")

funcionario = Funcionario("Diego", 25000, "Juiz Federal")
funcionario.aumentar_salario(12)
funcionario = Funcionario("Lourdes", 10000, "Analista Judiciária")
funcionario.aumentar_salario(15)

