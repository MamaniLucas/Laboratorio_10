numeros=[]
while True:
    n=int(input("Ingrese un numero: "))
    if n<=0:
        break
    numeros.append(n)
numeros.sort(reverse=True)
print(numeros)

