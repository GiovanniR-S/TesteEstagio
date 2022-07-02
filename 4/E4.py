valorTotal = 0.0;
dicionario = {"SP":67.83643, "RJ":36.67866, "MG":29.22988, "ES":27.16548, "Outros":19.84953}

for x in dicionario.values():
    valorTotal = valorTotal + x

resultado = (format(valorTotal, '.7f'))

print(f'{resultado}')
