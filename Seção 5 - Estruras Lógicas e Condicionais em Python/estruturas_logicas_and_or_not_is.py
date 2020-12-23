"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
    Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleando é invertido, ou seja, se for True, vira False, se for False, vira True.
Para o 'is', o vaor é comparado com um segundo.
"""

ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

ativo2 = True
logado2 = False

if ativo2 or logado2:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


ativo3 = False
logado3 = False

#   Jeito pythonico
if not ativo3:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

#   print(not False)

ativo4 = False
logado4 = False

if ativo4 is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

ativo5 = False
logado5 = False

if ativo5:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

#   ativo6 é falso?
ativo6 = False
print(ativo6 is False)
