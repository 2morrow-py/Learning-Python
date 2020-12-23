"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passsada como
parâmetro e como valor a quantidade de ocorrências desse elemento.

# Utilizando o Counter

# Realizando o import
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 43, 34]

# Utilizando o counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 1, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a
# quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""
from collections import Counter

# Exemplo 3

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue 
estabelecido na internet sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, 
objetivo e verificável​​, que todos possam editar e melhorar. O projeto é definido 
pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative Commons 
BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — 
desde que respeitando os termos e condições de uso.
Todos os editores da Wikipédia são voluntários. Eles integram uma comunidade colaborativa, 
sem um líder, na qual os membros coordenam os seus esforços no âmbito dos projetos 
temáticos e diversos espaços de discussão. Dentre as várias páginas de ajuda à disposição 
dos interessados em contribuir, estão as que explicam como criar um artigo ou editar 
um artigo. Em caso de dúvidas, não hesite em perguntar. Todos podem publicar conteúdo 
on-line desde que sigam as regras básicas estabelecidas pela comunidade, como por 
exemplo a verificabilidade da informação ou notoriedade do tema. Debates e comentários 
sobre os artigos são bem-vindos. As páginas de discussão servem para centralizar reflexões 
e avaliações sobre como melhorar o conteúdo da Wikipédia."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
