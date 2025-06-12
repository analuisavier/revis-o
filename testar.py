import os
os.system('cls' if os.name == 'nt' else 'clear')

a = 3
b = 2
x = 4
y = a * x + b 
print(y)

a = 3
b = 2
x = 4
y = a * x * b
print(y)

a = 3
b = 2
x = 4
y = a * a + b * b * x
print(y)

a = 3
b = 2
x = 4
y = a ** a + b ** b * x
print(y)

a = 3
b = 2
x = 4
y = a ** a / b ** b % x
print(y)

a = 3
b = a < 2 
x = 4
y = a < x or b 
print(y)

a = 3
b = a != 2
x = not b 
y = a == a and b or x
print(y)

a = 3
b = a < 2 
x = 4
y = a < x or b 
print(y)

a = int(3.5) 
b = "2" 
x = int("53")
y = a + int(b) + x
print(y)

a = "3"
b = "2"
x = "53"
y = a + b + x
print(y)

class Personagem:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

iron_man = Personagem("Tony Stark", 35)
capitao = Personagem("Steve Rogers", 25)
poder_total = iron_man.poder + capitao.poder
print(poder_total)

class Personagem:
    def __init__(self, nome, poder, pontos_vida=100):
        self.nome = nome
        self.poder = poder
        self.pontos_vida = pontos_vida

thanos = Personagem("Thanos", 120, 500)
hulk = Personagem("Hulk", 80, 300)
hulk.pontos_vida -= thanos.poder
print(hulk.pontos_vida)

class Personagem:
    def __init__(self, nome, poder, pontos_vida=100):
        self.nome = nome
        self.poder = poder
        self.pontos_vida = pontos_vida

thanos = Personagem("Thanos", 120, 500)
hulk = Personagem("Hulk", 80, 300)
hulk.pontos_vida -= thanos.poder

if hulk.pontos_vida < 0:
    print(f"{hulk.nome} foi derrotado")
else:
    print(f"{hulk.nome} ainda está de pé")

print(f"Pontos de vida do {hulk.nome}: {hulk.pontos_vida}")

class Personagem:
    def __init__(self, nome, poder, pontos_vida=100):
        self.nome = nome
        self.poder = poder
        self.pontos_vida = pontos_vida

thanos = Personagem("Thanos", 120, 500)
hulk = Personagem("Hulk", 80, 300)

num_golpes = 0
while hulk.pontos_vida >= 0:
    print(f"{thanos.nome} ataca {hulk.nome}")
    print(f"{hulk.nome} ainda está de pé")
    hulk.pontos_vida -= thanos.poder
    num_golpes += 1

print(f"Após {num_golpes} golpes, {thanos.nome} derrubou {hulk.nome}")

class Personagem:
    def __init__(self, nome, poder, velocidade, pontos_vida=100):
        self.nome = nome
        self.poder = poder
        self.velocidade = velocidade
        self.pontos_vida = pontos_vida

peter = Personagem("Homem Aranha", 50, 0.75, 200)
strange = Personagem("Doutor Estranho", 270, 0.4, 60)

alguem_perdeu = False

while not alguem_perdeu:
    print(f"{peter.nome} duela com {strange.nome}")
    peter.pontos_vida -= strange.poder * strange.velocidade 
    strange.pontos_vida -= peter.poder * peter.velocidade 
    
    if peter.pontos_vida <= 0:
        print(f"{peter.nome} perdeu todas as forças")
        alguem_perdeu = True

    elif strange.pontos_vida <= 0:
        print(f"{strange.nome} perdeu todas as forças")
        alguem_perdeu = True

a = 3
b = 5
resultado = 0
for i in range(b):
    resultado += a
print(resultado)

a = 2
b = 8
resultado = 1 
for i in range(b):
    resultado *= a
print(resultado)

def func1(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado

resultado = func1(3, 5)
print(resultado)
resultado = func1(2, 2)
print(resultado)


def func2(a, b):
    resultado = 0
    for i in range(b):
        resultado = func1(resultado, a)
    return resultado

resultado = func2(2, 3)
print(resultado)
resultado = func2(3, 1)
print(resultado)

def func3(a):
    resultado = 1
    if a > 0:
        resultado = a * func3(a - 1)
    return resultado

resultado = func3(2)
print(resultado)
resultado = func3(5)
print(resultado)

arcoiris = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta"]
print(arcoiris[0]) 
print(arcoiris[1])
print(arcoiris[-2])


alunos = ["Júlio", "Maria", "Ito", "Cleber"]
notas = [8.5, 9.0, 7.5, 6.0]
a = 0

for aluno in alunos:
    a += notas[alunos.index(aluno)]

b = a / len(alunos)
print(b)

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

alunos = [
    Aluno("Júlio", 8.5), 
    Aluno("Maria", 9.0), 
    Aluno("Ito", 7.5), 
    Aluno("Cleber", 9.5)
]

a = None
for aluno in alunos:
    if a is None:
        a = aluno
    else:
        if aluno.nota > a.nota:
            a = aluno

print(f"{a.nome}: {a.nota}")


inteiro = 5
float_num = 3.5
resultado = inteiro * float_num
print(resultado)

a = 1117.7
b = 221.1  
c = 13.3
resultado = a // b // c
print(resultado)

nomes_femininos = ["Maria", "Ana", "Clara"]
termo_tratamento = "Sra."
nomes_com_tratamento = [termo_tratamento + " " + nome for nome in nomes_femininos]
print(nomes_com_tratamento)

soma = 0
for i in range(1, 101):
    soma += i
    print(soma)
    
soma = 0
for i in range(1, 101):
    if i % 2 != 0:
        soma += i
print(soma)    
    
while True:
    print("Menu:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Frango à Parmigiana com batata frita e uma coca-cola.")
    elif escolha == "2":
        print("Executivo de carne de sol.")
    elif escolha == "3":
        print("Saindo do menu...")
        break
    else:
        print("Opção inválida, tente novamente.")
        
import math

a = 4
b = 2
c = -10
delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes da equação são: {raiz1} e {raiz2}")   
    

def soma_impares(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma += i
    return soma 

n = 100  
print(f"A soma dos números ímpares de 1 a {n} é: {soma_impares(n)}")

if soma_impares(n) == n ** 2:
    print("A soma dos N primeiros ímpares é igual a N ao quadrado!")
else:
    print("A soma dos N primeiros ímpares NÃO é igual a N ao quadrado.")


def multiplica_inteiro_float(inteiro, float_num):
    resultado = inteiro * float_num

def divide_inteiros(a, b, c):
    resultado = a // b // c

def tratamento_nomes(nomes_femininos, termo_tratamento):
    nomes_com_tratamento = [termo_tratamento + " " + nome for nome in nomes_femininos]
    
def soma_numeros(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma      

def soma_impares(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma += i
    return soma

def menu_opcoes():
    while True:
        print("Menu:")
        print("1. Opção 1")
        print("2. Opção 2")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print("Frango à Parmigiana com batata frita e uma coca-cola.")
        elif escolha == "2":
            print("Executivo de carne de sol.")
        elif escolha == "3":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida, tente novamente.")  

def bhaskara(a, b, c):
    import math
    delta = b**2 - 4*a*c

    if delta < 0:
        return "A equação não possui raízes reais."
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"As raízes da equação são: {raiz1} e {raiz2}"

def soma_impares_quadrado(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma += i
    return soma

def verifica_soma_impares_quadrado(n):
    if soma_impares_quadrado(n) == n ** 2:
        return "A soma dos N primeiros ímpares é igual a N ao quadrado!"
    else:
        return "A soma dos N primeiros ímpares NÃO é igual a N ao quadrado."
    

import random

class Poder:
    def __init__(self, nome_poder, dano):
        self.nome_poder = nome_poder
        self.dano = dano

poder1 = Poder("Rajada de Energia", 30)
poder2 = Poder("Golpe de Fúria", 25)
poder3 = Poder("Rajada de Gelo", 20)
poder4 = Poder("Chuva de Meteoros", 50)                

class Personagem:
    def __init__(self, nome, poderes, pontos_vida=100):
        self.nome = nome
        self.poderes = poderes
        self.pontos_vida = pontos_vida        

Julio = Personagem("Júlio", [poder1, poder2], 100)
Maria = Personagem("Maria", [poder3, poder4], 100)

while Julio.pontos_vida > 0 and Maria.pontos_vida > 0:
    poder_julio = random.choice(Julio.poderes)
    poder_maria = random.choice(Maria.poderes)
    
    print(f"{Julio.nome} usa {poder_julio.nome_poder} causando {poder_julio.dano} de dano.")
    Maria.pontos_vida -= poder_julio.dano
    
    if Maria.pontos_vida <= 0:
        print(f"{Maria.nome} foi derrotada!")
        break
    
    print(f"{Maria.nome} usa {poder_maria.nome_poder} causando {poder_maria.dano} de dano.")
    Julio.pontos_vida -= poder_maria.dano
    
    if Julio.pontos_vida <= 0:
        print(f"{Julio.nome} foi derrotado!")
        break