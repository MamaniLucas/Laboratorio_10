sueldos=(100, 5000, 10000, 525, 15)
i=0
max = sueldos[0]
min = sueldos[0]
while i <5:
    if min > sueldos [i]:
       min=sueldos [i]
    if max < sueldos [i]:
        max=sueldos[i]
    i+=1
print("el menor sueldo es: ", min)
print("el mayor sueldo es: ", max)

