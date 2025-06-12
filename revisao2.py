# Para todos os exercícios abaixo, caso exista algum erro claro
# corrija o código e então responda a pergunta.

# Questão. defina o valor e tipo da variável y
a = 3
b = 2
x = 4
y = a * x + b 
print(y)

#começar pela multiplicação e depois somar 
#resulta em: y = 3 * 4 = 12 
# 12 + 2 = 14 
#14 do tipo int (inteiro)
#CORRETAAAAAAAAAAA

# Questão. defina o valor e tipo da variável y
a = 3
b = 2
x = 4
y = a * x * b
print(y)
#Aqui, a multiplicação é feita entre a, x e b
#resulta em: y = 3 * 4 * 2 = 24
#24 do tipo int (inteiro)
#CORRETAAAAAAAAAAA

# Questão. defina o valor e tipo da variável y
a = 3
b = 2
x = 4
y = a * a + b * b * x
print(y)

# Aqui, a multiplicação é feita entre a, b e x
#resulta em: y = 3 * 3 + 2 * 2 * 4
#resulta em: y = 9 + 16
#resulta em: y = 25
#25 do tipo int (inteiro)
#CORRETAAAAAAAAAAA

# Questão. defina o valor e tipo da variável y
a = 3
b = 2
x = 4
y = a ** a + b ** b * x
print(y)
# Aqui, a exponenciação é feita entre a e b
#resulta em: y = 3 ** 3 + 2 ** 2 * 4
#resulta em: y = 3 * 3 * 3 = 27 
#resulta em: y = 27 + 4 * 4
#resulta em: y = 27 + 16
#resulta em: y = 43
#43 do tipo int (inteiro)
#CORRETAAAAAAAAAAA

# Questão. defina o valor e tipo da variável y
a = 3
b = 2
x = 4
y = a ** a + b ** b * x
print(y)

# Aqui, a exponenciação é feita entre a e b
#resulta em: y = 3 ** 3 + 2 ** 2 * 4    
#resulta em: y = 3 * 3 * 3 = 27
#resulta em: y = 27 + 4 * 4
#resulta em: y = 27 + 16
#resulta em: y = 43
#43 do tipo int (inteiro)
#CORRETAAAAAAAAAAA

# Questão. defina o valor e tipo da variável y
a = 3
b = 2
x = 4
y = a ** a / b ** b % x
print(y)

# Aqui, a exponenciação é feita entre a e b
#resulta em: y = 3 ** 3 / 2 ** 2 % 4
#resulta em: y = 27 / 4 % 4
#resulta em: y = 6.75 % 4
#resulta em: y = 2.75
#2.75 do tipo float (ponto flutuante)
#CORRETAAAAAAAAAAA


# Questão. defina o valor e tipo da variável y
a = 3
b = a < 2 (false)
x = 4
y = a < x or b (true)
print(y)

# Aqui, a comparação é feita entre a e x
#resulta em: y = 3 < 4 or False
#resulta em: y = True or False
#resulta em: y = True
#True do tipo bool (booleano)
#CORRETAAAAAAAAAAA

# Questão. defina o valor e tipo da variável y
a = 3
b = a != 2 (true)
x = not b (false)
y = a == a and b or x
print(y)

# Aqui, a comparação é feita entre a e b
#resulta em: y = 3 == 3 and True or False
#resulta em: y = True and True or False
#resulta em: y = True or False
#resulta em: y = True
#True do tipo bool (booleano)

# Questão. defina o valor e tipo da variável y
a = int(3.5) (3)
b = "2" # (string)
x = int("53") # (53)
y = a + int(b) + x
print(y)

# Aqui, a conversão de tipos é feita
#resulta em: y = 3 + 2 + 53
#resulta em: y = 58
#58 do tipo int (inteiro)


# Questão. defina o valor e tipo da variável y
a = "3"
b = "2"
x = "53"
y = a + b + x
print(y)

# Aqui, a concatenação de strings é feita
#resulta em: y = "3" + "2" + "53"   
#resulta em: y = "3253"
#"3253" do tipo str (string)

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# ex.: linha 74, depois 75, 76, etc. ou, linha 80, depois 81, depois 75.
# escreva a ordem de execução das linhas de código desta questão.
# e depois indique o valor impresso na tela ao final.
class Personagem:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

iron_man = Personagem("Tony Stark", 35)
capitao = Personagem("Steve Rogers", 25)
poder_total = iron_man.poder + capitao.poder
print(poder_total)

# A ordem de execução das linhas de código é:
# 1. Linha 1: definição da classe Personagem
# 2. Linha 2: definição do método construtor __init__
# 3. Linha 4: criação do objeto iron
# 4. Linha 5: criação do objeto capitao
# 5. Linha 6: cálculo do poder total
# 6. Linha 7: impressão do poder total
# O valor impresso na tela ao final é 60, que é a soma dos poderes de   


# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# e qual é o valor impresso na tela ao final?
class Personagem:
    def __init__(self, nome, poder, pontos_vida=100):
        self.nome = nome
        self.poder = poder
        self.pontos_vida = pontos_vida

thanos = Personagem("Thanos", 120, 500)
hulk = Personagem("Hulk", 80, 300)
hulk.pontos_vida -= thanos.poder
print(hulk.pontos_vida)

# A ordem de execução das linhas de código é:
# 1. Linha 1: definição da classe Personagem
# 2. Linha 2: definição do método construtor __init__
# 3. Linha 4: criação do objeto thanos
# 4. Linha 5: criação do objeto hulk
# 5. Linha 6: subtração do poder de thanos dos pontos de vida de hulk
# 6. Linha 7: impressão dos pontos de vida de hulk
# O valor impresso na tela ao final é 220, que é o resultado de 300 - 120.

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# e quais são os valores impressos na tela ao final?
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

#1 linha: definição da classe Personagem
#2 linha: definição do método construtor __init__
#3 linha: criação do objeto thanos
#4 linha: criação do objeto hulk
#5 linha: subtração do poder de thanos dos pontos de vida de hulk
#6 linha: verificação se os pontos de vida de hulk são menores que 0  
#7 linha: impressão se hulk foi derrotado ou ainda está de pé
#8 linha: impressão dos pontos de vida de hulk
# O valor impresso na tela ao final é:
# "Hulk ainda está de pé" e "Pontos de vida do Hulk: 220", pois 300 - 120 = 180, que é maior que 0.

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# e quais são os valores impressos na tela ao final?
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

# A ordem de execução das linhas de código é:
# 1. Linha 1: definição da classe Personagem
# 2. Linha 2: definição do método construtor __init__
# 3. Linha 4: criação do objeto thanos
# 4. Linha 5: criação do objeto hulk
# 5. Linha 7: inicialização da variável num_golpes
# 6. Linha 8: início do loop while que continua enquanto os pontos de vida de hulk forem maiores ou iguais a 0
# 7. Linha 9: impressão da mensagem de ataque de thanos a hulk
# 8. Linha 10: impressão de que hulk ainda está de pé
# 9. Linha 11: subtração do poder de thanos dos pontos de vida de hulk
# 10. Linha 12: incremento do contador de golpes
# 11. Linha 14: impressão do número total de golpes e que thanos derrubou hulk

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# e quais são os valores impressos na tela ao final?
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
        
# A ordem de execução das linhas de código é:
# 1. Linha 1: definição da classe Personagem
# 2. Linha 2: definição do método construtor __init__
# 3. Linha 4: criação do objeto peter
# 4. Linha 5: criação do objeto strange
# 5. Linha 7: inicialização da variável alguem_perdeu como False   
# 6. Linha 9: início do loop while que continua enquanto alguem_perdeu for False
# 7. Linha 10: impressão da mensagem de duelo entre peter e strange
# 8. Linha 11: subtração do poder de strange multiplicado pela velocidade de strange dos pontos de vida de peter
# 9. Linha 12: subtração do poder de peter multiplicado pela velocidade de peter dos pontos de vida de strange
# 10. Linha 14: verificação se os pontos de vida de peter são menores ou iguais a 0
# 11. Linha 15: impressão de que peter perdeu todas as forças e definição de alguem_perdeu como True
# 12. Linha 18: verificação se os pontos de vida de strange são menores ou iguais a 0
# 13. Linha 19: impressão de que strange perdeu todas as forças e definição de alguem_perdeu como True
# O valor impresso na tela ao final depende de quem perdeu primeiro, mas o loop continuará até que um dos personagens perca todas as forças.
# Homem Aranha perdeu todas as forças

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

a = 3
b = 5
resultado = 0
for i in range(b):
    resultado += a
print(resultado)

# A ordem de execução das linhas de código é:
# 1. Linha 1: atribuição do valor 3 à variável a 
# 2. Linha 2: atribuição do valor 5 à variável b
# 3. Linha 3: inicialização da variável resultado com o valor 0
# 4. Linha 4: início do loop for que itera b vezes (5 vezes)
# 5. Linha 5: adição do valor de a (3) à variável resultado em cada iteração do loop
# 6. Linha 6: impressão do valor final de resultado após o loop
# O propósito do código é calcular a soma de 3 repetido 5 vezes, ou seja, 3 + 3 + 3 + 3 + 3.
# O valor impresso na tela ao final é 15, que é o resultado da soma de 3 cinco vezes.

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

a = 2
b = 8
resultado = 1 
for i in range(b):
    resultado *= a
print(resultado)

#criou a variavel a e b
# A ordem de execução das linhas de código é:
# 1. Linha 1: atribuição do valor 2 à variável a
# 2. Linha 2: atribuição do valor 8 à variável b
# 3. Linha 3: inicialização da variável resultado com o valor 1
# 4. Linha 4: início do loop for que itera b vezes (8 vezes)
# 5. Linha 5: multiplicação do valor de a (2) pelo valor atual de resultado em cada iteração do loop
# 6. Linha 6: impressão do valor final de resultado após o loop
# O propósito do código é calcular 2 elevado a 8, ou seja, 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2.
# O valor impresso na tela ao final é 256, que é o resultado de 2 elevado a 8.

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

a = 5
resultado = 1
while a > 0:
    resultado *= a
    a -= 1

# A ordem de execução das linhas de código é:
# 1. Linha 1: atribuição do valor 5 à variável a   
# 2. Linha 2: inicialização da variável resultado com o valor 1
# 3. Linha 3: início do loop while que continua enquanto a for maior que 0
# 4. Linha 4: multiplicação do valor atual de resultado pelo valor de a
# 5. Linha 5: decremento do valor de a em 1
# O propósito do código é calcular o fatorial de 5, ou seja, 5! = 5 * 4 * 3 * 2 * 1.
# O valor impresso na tela ao final é 120, que é o resultado do fatorial de 5.

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

def func1(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado

resultado = func1(3, 5)
print(resultado)
resultado = func1(2, 2)
print(resultado)

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

def func2(a, b):
    resultado = 0
    for i in range(b):
        resultado = func1(resultado, a)
    return resultado

resultado = func2(2, 3)
print(resultado)
resultado = func2(3, 1)
print(resultado)

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

def func3(a):
    resultado = 1
    if a > 0:
        resultado = a * func3(a - 1) 
    return resultado

resultado = func3(2) 
print(resultado)
resultado = func3(5)
print(resultado)

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

arcoiris = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta"]
print(arcoiris[0]) 
print(arcoiris[1])
print(arcoiris[-2])

# 1. Linha 1: criação da lista arcoiris com as cores do arco-íris
# 2. Linha 2: impressão do primeiro elemento da lista (índice 0), que é "Vermelho"
# 3. Linha 3: impressão do segundo elemento da lista (índice 1), que é "Laranja"
# 4. Linha 4: impressão do penúltimo elemento da lista (índice -2), que é "Anil"


# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

alunos = ["Júlio", "Maria", "Ito", "Cleber"]
notas = [8.5, 9.0, 7.5, 6.0]
a = 0

for aluno in alunos:
    a += notas[alunos.index(aluno)]

b = a / len(alunos)
print(b)

# Questão.
# qual é a ordem de execução das linhas de código desta questão?
# qual é o propósito do código? o que o desenvolveder queria quando escreveu?
# e quais são os valores impressos na tela ao final?

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

# Questão.
# prática, escreva um código que
# cria duas variáveis e atribui a elas valores numéricos
# sendo um float e outro inteiro, e depois multiplica esses valores
# e imprime o resultado na tela.

inteiro = 5
float_num = 3.5
resultado = inteiro * float_num
print(resultado)

# Questão.
# prática, escreva um código que
# cria três variáveis float 1117.7, 221.1 e 13.3, realiza a divisão inteira //
# em cascata das variáveis, ex.: a // b // c,
# e imprime o resultado na tela.

a = 1117.7
b = 221.1  
c = 13.3
resultado = a // b // c
print(resultado)

# Questão.
# prática, escreva um código que
# adiciona um termo de tratamento "Sra." a uma strings de nome feminino
# e imprime o resultado na tela.

nome_feminino = "Maria"
termo_tratamento = "Sra."
nome_com_tratamento = termo_tratamento + " " + nome_feminino
print(nome_com_tratamento)

# Questão.
# prática, escreva um código que
# adiciona um termo de tratamento "Sra." a uma lista de strings de nomes femininos
# e imprime o resultado na tela.

nomes_femininos = ["Maria", "Ana", "Clara"]
termo_tratamento = "Sra."
nomes_com_tratamento = [termo_tratamento + " " + nome for nome in nomes_femininos]
print(nomes_com_tratamento)

# Questão.
# prática, escreva um código que
# calcula a soma dos números de 1 a 100
# e imprime o resultado na tela.

soma = 0
for i in range(1, 101):
    soma += i
print(soma)

# Questão.
# prática, escreva um código que
# calcula a soma somente os números ímpares de 1 a 100
# e imprime o resultado na tela.

soma = 0
for i in range(1, 101):
    if i % 2 != 0:
        soma += i
print(soma)

# Questão.
# prática, escreva um código que
# acusa se um número é primo ou não
# e imprime o resultado na tela.

numero = 20
if numero < 2:
    print(f"{numero} não é primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é primo")
            break
        else:
            print(f"{numero} é primo")
            break

# Questão.
# prática, escreva um código que
# oferta um menu com 3 opções e só sai quando o usuário escolhe 3

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


# Questão.
# prática, escreva um código que
# calcula a raiz de uma equação quadrática
# usando a fórmula de Bhaskara
# e imprime o resultado na tela da raiz dos valores de a = 4, b = 2 e c = -10

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

# Questão.
# prática, escreva um código que
# calcula a soma dos N números ímpares de 1 a N
# e imprime o resultado na tela.

def soma_impares(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma += i
    return soma 

n = 100  
print(f"A soma dos números ímpares de 1 a {n} é: {soma_impares(n)}")

# Questão.
# prática, escreva um código que
# mostra que a soma dos N números ímpares de 1 a N
# é igual a potência de N ao quadrado, N ** 2
# e imprime o resultado na tela.

def soma_impares(n):
    soma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma += i
    return soma

N = 10 
print(f"Soma dos {N} primeiros ímpares: {soma_impares(N)}")
print(f"{N} ao quadrado: {N ** 2}")

if soma_impares(N) == N ** 2:
    print("A soma dos N primeiros ímpares é igual a N ao quadrado!")
else:
    print("A soma dos N primeiros ímpares NÃO é igual a N ao quadrado.")

# Questão.
# prática, escreva um código que
# cria uma função para cada um dos códigos acima

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
        
# Questão.
# prática, escreva um código que
# define uma classe 'poder' com o nome do poder e o dano causado
# define uma classe 'personagem' com atributos nome, poderes e pontos de vida
# crie quatro objetos da classe 'poder' diferentes, para dois personagens diferentes
# crie dois objetos da classe 'personagem' com poderes diferentes
# crie um laço que simula um duelo entre os dois personagens em que
# cada personagem ataca o outro com um poder aleatório 
# até que um deles perca todos os pontos de vida

import random

class Poder:
    def __init__(self, nome_poder, dano):
        self.nome_poder = nome
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