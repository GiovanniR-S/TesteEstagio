valor = int(input());
x = 0;
y = 1;
aux = 0;

while True:
    
    if (valor < 0):
          print("Numero Inválido")
          break;

    elif (valor == x or valor == y):
          print("É Fibonacci");
          break;
        
    elif (y > valor):   
        print("Não é Fibonacci");
        break;
        
    else:
        aux = x
        x = y;
        y = aux + y;

            

