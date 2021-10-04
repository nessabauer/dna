import sys
import csv

# Utilizando o programa da forma correta com 3 parâmetros
if len(sys.argv) != 3:
    sys.exit("Usage: python dna.py CSV_FILE TEXT_FILE")

num_row = 0
# Lendo o CSV dentro de uma variável dict e contando as linhas
database = {}
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        num_row += 1
        for column, value in row.items():
            database.setdefault(column, []).append(value)

# Lendo o TXT dentro de uma variável
with open(sys.argv[2]) as f:
    dna = f.read()

match = []
match_bkp = []

# inicializando a lista de match
for m in range(num_row-1):
    match.append(m)

# for em todas as chaves
for key in database.keys():
    contador = 0
    maximo = 0
    # descartando o nome
    if key != 'name':
        # Procurando o primeiro match do DNA
        for i in range((len(dna)-len(key))):
            if dna[i:(len(key)+i)] == key:
                # Encontrando o primeiro, somando as repetições
                for k in range(i, ((len(dna)-len(key))), len(key)):
                    if dna[k:(len(key)+k)] == key:
                        contador += 1
                    else:
                        # Se as repições forem maiores que a anterior substitui
                        if contador > maximo:
                            maximo = contador
                        contador = 0
                        break

        # Varendo os nomes a procura de matchs com aquele total
        for m in range(num_row-1):
            if int(database[key][m]) == maximo:
                # Se não tiver na variável match é pq os valores anteriores não fecharam somente o atual
                if match.count(m) > 0:
                    match_bkp.append(m)

        # Se não achou nenhum que combine sai do programa e "No match"
        if len(match_bkp) == 0:
            print('No match')
            exit()

        # Salvando os novos matchs
        match.clear()
        match = match_bkp.copy()
        match_bkp.clear()

print(database["name"][match[0]])

