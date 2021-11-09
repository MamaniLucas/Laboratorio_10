numeros=[]
while True:
    n = int(input("Ingrese un numero: "))
    if n <=0:
        break
    numeros.append(n)
print(sorted(numeros))