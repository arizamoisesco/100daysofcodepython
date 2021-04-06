#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
numero_aleatoria = random.randint(0, len(word_list)-1)
palabra_aleatoria = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letra_usuario = input("Ingrese la letra: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letras in palabra_aleatoria:
    if letras == letra_usuario:
        print("Bien")
    else:
        print("Mal")