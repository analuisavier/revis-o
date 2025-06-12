# -----------------------------------------------------
# Tema 1: IDE, estilo e erros
# -----------------------------------------------------

player_health = 100
if player_health > 0      # qual o erro? tipo?
    print("Jogador está vivo")

player_name = "Guerreiro"
print("Bem-vindo, " + playerName)  # qual o erro? tipo?

def setup_character():
·print("Inicializando personagem...")  # este ponto inicial tem um caractere diferente antes de 'print': o que causa o erro? tipo?
    print("Personagem pronto")

def calculate_score( xp, bonus   ):
    total = xp + bonus
    return  total    
print(calculate_score( 50,20 ))

# -----------------------------------------------------
# Tema 2: Variáveis e operações
# -----------------------------------------------------


coins_found = 7
coins_spent = 3
gold = coins_found + coins_spent * 2
print(gold)  # qual o valor de 'gold'?

health = 0
is_alive = health > 0
print(is_alive)  # qual o valor de 'is_alive'?

xp = 150
bonus = 20
total_xp = xp + bonus // 2   # qual o valor de total_xp? qual o tipo de total_xp?
print(total_xp)

level = "5"
bonus = 2
new_level = level + bonus # qual o valor e tipo de new_level?

level = "5"
bonus = "2"
new_level = level + bonus # qual o valor e tipo de new_level?

level = "5"
bonus = 2
new_level = int(level) + bonus # qual o valor e tipo de new_level?

a = b = [1, 2, 3]
a.append(4)
print(b)  # qual o valor de 'b'?

coins = 10.5
remainder = coins % 3 # qual é o valor de 'remainder'?

strength = 10
armor = 5
damage = strength - armor > 3 and strength + armor < 20 or False
print(damage)  # qual o valor de 'damage'? Explique a precedência lógica nesse contexto.

# -----------------------------------------------------
# Tema 3: Objetos, entrada e saída de texto
# -----------------------------------------------------

# qual o erro? tipo?
player_name = input("Digite seu nome: )  

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

e = Enemy("Orc", 50)
print(e.name)  # qual o valor impresso?

class Player:
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory

p1 = Player("Alice")
p2 = Player("Bob")
p1 = p2
p1.inventory.append("Espada")
print(p2.inventory)  # qual o valor de p2.inventory? 

name = "Global"
class NPC:
    name = "NPC"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Olá, " + name

npc = NPC("Guardião")
print(npc) # o que é impresso?

def use_potion(player_hp):
    if player_hp < 50:
        player_hp += potion_strength
    return player_hp

potion_strength = 20
novo_hp = use_potion(30)
print(novo_hp)  

# -----------------------------------------------------
# Tema 4: Condicionais
# -----------------------------------------------------

level = "10"
if level == 10:
    print("Nível 10 alcançado!") 

quest_completed = False
reward = 100 if quest_completed else 0
print(reward)  # qual o valor de 'reward'?

hp = 0
mp = 10
if hp > 0 and (mp / hp) > 2: 
    print("Pontos de magia suficientes")
else:
    print("Incapacitado")

# qual é o resultado do código acima?

# Q25 (difícil): Uso de 'is' para comparar literais e objetos mutáveis.
a = [1, 2, 3]
b = [1, 2, 3]
if a is b:
    print("Mesma lista")
else:
    print("Listas diferentes") 

# qual o resultado? Qual a armadilha de 'is' vs '=='?

level = 7
if 5 < level < 10:
    print("Intermediário")
else:
    print("Fora de intervalo")  

# qual o valor impresso?

has_key = True
gold = 50
can_enter = has_key and gold > 100 or gold == 50
print(can_enter)  # qual o valor de 'can_enter'?

mana = 20
if mana > 30:
    print("Magia forte")
elif mana > 10:
    print("Magia média")
else:
    print("Sem mana")  

# qual a sequência de impressão aqui?

items = []
if items:
    print("Inventário cheio")
else:
    print("Inventário vazio")  

# o que será impresso?

# -----------------------------------------------------
# Tema 5: Laços e listas
# -----------------------------------------------------

enemies = ["Goblin", "Orc", "Troll"]
for enemy in enemies:
    print(enemy)  

# qual a sequência de saídas?

count = 0
while count < 3:
    print(count)
    count += 1  

# qual a última valor impresso?

inventory = ["Espada", "Poção", "Elixir"]
for item in inventory:
    if item == "Poção":
        inventory.remove(item)
print(inventory)  

# qual o conteúdo final de 'inventory'?

items = ["Espada", "Escudo"]
print(items[-1])  
# qual é o resultado da impressão?

for i in range(0, 5, 0):
    print(i)  
# qual é a impressão?

# -----------------------------------------------------
# Tema 6: Funções e pilha de chamadas
# -----------------------------------------------------

def heal(hp, potion=20):
    return hp + potion

hp_after = heal(30)
print(hp_after)  # qual o valor impresso?

def attack(damage):
    print(f"Dano causado: {damage}")

attack(15)  # o que é exibido?

def add_buff(buffs=[]):
    buffs.append("Força")
    return buffs

b1 = add_buff()
b2 = add_buff()
print(b1, b2)  # qual o valor de ambas as listas?

def infinite(n):
    return print(infinite(n + 1))

infinite(1)  # o que será impresso?

def calculate(value):
    return value * 2

calculate = 10
print(calculate(5))  # qual o valor impresso?

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

def create_enemy(name, hp, attack):
    return Character(name, hp, attack)

enemy = create_enemy("Dragão", attack=50, 200)  
print(enemy.hp)  # qual o valor impresso?

def buff(player_hp):
    if player_hp < 100:
        player_hp += extra_hp
    extra_hp = 20
    return player_hp

print(buff(80))  # qual o valor impresso?

def deep_recursion(n):
    print(n)
    if n == 0:
        return "fim"
    return deep_recursion(n - 1)

deep_recursion(-10) # o que será impresso?