#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
palabra_aleatoria = random.choice(word_list)
#Testing 
print(f"La palabra es {palabra_aleatoria}")
espacio_blanco = []
#Generar lista aleatoria con espacios en blanco
for palabra in palabra_aleatoria:
    espacio_blanco.append("_")

print(espacio_blanco)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letra_usuario = input("Ingrese la letra: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letras in palabra_aleatoria:
    if letras == letra_usuario:
        indice = palabra_aleatoria.index(letras)
        espacio_blanco[indice] = letras
        print(espacio_blanco)
    else:
        print("Mal")