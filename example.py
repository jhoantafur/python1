"""
Ejemplo con while
while True:
    print("Atrapado en un bucle infinito.")

Ejemplo 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

Ejemplo 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Ejemplo 2
for i in range(1, 10):
   if i % 2 == 0:
        print(i)


#Sentencias Break
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")



text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

#Setencias condicionales con else


n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

for i in range(0, 3):
    print(i)
else:
    print(i, "else")



for i in range(3):
    print(i, end=" ")  # output: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # output: 6, 4, 2
"""