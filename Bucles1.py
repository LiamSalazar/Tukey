print("------------------------------")
print("FOR:")
print("------------------------------")
for numero in range(5):
    print(numero)
count = 1
print("------------------------------")
print("WHILE:")
print("------------------------------")
while count <= 5:
    print(count)
    count += 1
lista = ["Insano", "Angel", "Diego"]
print("------------------------------")
print("NOMBRES:")
print("------------------------------")
for nombre in lista:
    if nombre == "Insano":
        continue
    print(nombre)
print("------------------------------")
print("SUMA:")
print("------------------------------")
nums = [1,1,1,1]
suma = 0
for num in nums:
    suma += num
print(suma)