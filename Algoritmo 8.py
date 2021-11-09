names=["Luna","sol","Fenix","Oríon"]
while True:
    number = int(input("Numero: "))
    if number <= 0:
        print("El numero debe ser mayor a 0")
        break
    print(names[number - 1])
