
user_word = input("Ingresa la palabra que desees ")
largoLetra = len(user_word)
word_without_vowels = ""
letter = 0
i = 0
#HOLA
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
        word_without_vowels += user_word[i]
        i += 1
print(word_without_vowels)




