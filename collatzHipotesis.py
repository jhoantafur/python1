c0 = int(input())   # leemos el número natural inicial

pasos = 0           # contador de transformaciones

while c0 != 1:
    if c0 % 2 == 0:        # ¿es par?
        c0 = c0 // 2       # sí → lo divido entre 2
    else:                  # si no, es impar
        c0 = 3 * c0 + 1    # impar → 3·c0 + 1
    print(c0)              # muestro el nuevo valor
    pasos += 1             # conté un paso más

print("pasos =", pasos)