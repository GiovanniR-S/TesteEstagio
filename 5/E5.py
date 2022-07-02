string = "Teste de frase com espaços"
aux = []
reverseString = ""
i = 0

for x in string:
    aux.append(x)

while(i < len(aux)):
    if(i == 0):
        reverseString = reverseString + aux[len(aux) - 1]
        i = i + 1
    else:
        reverseString = reverseString + aux[(len(aux) - 1) - i]
        i = i + 1

print(reverseString)
