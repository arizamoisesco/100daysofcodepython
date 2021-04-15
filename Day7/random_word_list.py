#Step 1 
import random
import arte_ahorcado as dibujos
import palabras_ahorcado as palabras

print(dibujos.logo)
estados = dibujos.stages

word_list = palabras.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
palabra_aleatoria = random.choice(word_list)
#Testing 
print(f"La palabra es {palabra_aleatoria}")
espacio_blanco = []
#Generar lista aleatoria con espacios en blanco
for palabra in palabra_aleatoria:
    espacio_blanco.append("_")

print(espacio_blanco)
#cantidad_caracteres = len(palabra_aleatoria)
fin_juego = False
oportunidad = 6
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while not fin_juego == True:
    letra_usuario = input("Ingrese la letra: ").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for posicion in range(len(palabra_aleatoria)):
        
        letra = palabra_aleatoria[posicion]

        if letra in espacio_blanco:
          print("Ya usaste esta letra")
        else:
          if letra == letra_usuario:
            print(estados[oportunidad])
            espacio_blanco[posicion] = letra

    if letra_usuario not in palabra_aleatoria:
      print("Lo siento haz perdido una vida")
      oportunidad -= 1
      print(estados[oportunidad])
      if oportunidad == 0:
        fin_juego = True
        print("Lo siento perdiste")     

        
            

    print(espacio_blanco)
    
    if "_" not in espacio_blanco:
        fin_juego = True
        print("Tu ganas")

   # else:
   #     print("Mal")
