# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa la palabra que desees ")
largoLetra = len(user_word)
#letras = ["A","E","I","O","U"]
letter = 0
i = 0
#I[0], N[1], D[2], I[3], R[4], A[5]
user_word = user_word.upper()
for letter in user_word:
    if (user_word[i] == 'A'):
        i += 1
        continue
    elif (user_word[i] == 'E'):
        i += 1
        continue
    elif (user_word[i] == 'I'):
        i += 1
        continue
    elif (user_word[i] == 'O'):
        i += 1
        continue
    elif (user_word[i] == 'U'):
        i += 1
        continue
    else:
        print(user_word[i])
        i += 1








