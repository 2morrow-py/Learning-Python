"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualqeur coisa, desde que comece com asterísco.

# Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O Parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos não legais

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 6))   # TypeError
# print(soma_todos_numeros(4, 6, 9, 7))   # TypeError

# Solução exemplo não legais

def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))
# print(soma_todos_numeros(4, 6, 9, 7))   # TypeError

# Entendendo o *args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))

# Refatorando Exemplo (melhorando)

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))
# print(soma_todos_numeros('a'))   # TypeError

# Outro exempl ode utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University1', 3.145))

"""

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1, 2, 3, 4, 5))

numeros = [1, 2, 3, 4, 5, 6, 7]

# print(soma_todos_numeros(numeros))   # TypeError

# Desempacotador (solução)

print(soma_todos_numeros(*numeros))

# OBS: O asterísco serve para que informemos ao Python que estamos passando como
# argumento uma coleção de dados. Desta forma, ele saberá que precisará antes
# desempacotar estes dados.