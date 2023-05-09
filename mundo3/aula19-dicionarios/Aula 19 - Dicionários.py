
pessoas = {'nome': 'Victor', 'sexo': 'Masculino', 'idade': 18}

print(f'\nO {pessoas["nome"]} é do sexo {pessoas["sexo"]} e tem {pessoas["idade"]} anos.\n')

print(pessoas.keys(), '\n')
print(pessoas.values(), '\n')

print(pessoas.items(), '\n')

for k, v in pessoas.items():
    print(f'{k} = {v}\n')

# del pessoas["nome"]

# pessoas["nome"] = "Lolo"

# pessoas["peso"] = 90

brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)


print(estado1, '\n')
print(estado2, '\n')
print(brasil, '\n')
print(brasil[0]['uf'], '\n')
print(brasil[1]['sigla'], '\n')
