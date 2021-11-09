lista=[]
n= int(input("Ingrese numero: "))
for i in range(1, 13):
    resul = n*i
    a = str(n)+"x"+str(i)+"="+str(resul)
    lista.append(a)
for i in lista:
    print(i)
print(lista)
