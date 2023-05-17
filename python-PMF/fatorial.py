fatorial = numero = int(input("qual número para calc. fatorial: "))

while numero > 1:
    numero = numero - 1
    fatorial = fatorial*numero
    print(fatorial)
print("o resultado",fatorial)