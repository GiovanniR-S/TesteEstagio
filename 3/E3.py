# Importar o módulo
import json

with open("dados.json") as file:
    dados = json.load(file)

menorDia = dados[len(dados) - 1]["dia"]
menorValorDia = dados[len(dados) - 1]["valor"]
mediaMensal = 0
dias = 0
diasAcimaDaMedia = 0

# Pegar menor dia
for x in dados:
    if(x["dia"] == 0):
        continue;
    else:
        if(x["dia"] < menorDia):
            menorDia = x["dia"]
        else:
            break;

# Pegar menor Valor
for y in dados:
    if(y["valor"] == 0):
        continue;
    else:
        if(y["valor"] < menorValorDia):
            menorValorDia = y["valor"]
        else:
            continue;

# Media Mensal    
for m in dados:
    if(m["valor"] == 0):
        continue
    else:
        dias = dias + 1
        mediaMensal = mediaMensal + m["valor"]

mediaMensal = mediaMensal/dias

# Dias acima da média
for d in dados:
    if(d["valor"] > mediaMensal):
        diasAcimaDaMedia = diasAcimaDaMedia + 1
    else:
        continue

print("Quantidades de Dias sem faturamentos: ", len(dados))
print("Quantidades de Dias com faturamentos: ", dias)
print("Menor Dia: ", menorDia)
print("Menor Valor Dia: ", menorValorDia)
print("Media Mensal: ", mediaMensal)
print("Dias acima da media: ", diasAcimaDaMedia)
