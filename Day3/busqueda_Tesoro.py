print('''   
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Bienvenido a la aventura\n Tu misión sera enontrar el tesoro")
opcion = input("Selecciona hacia que lado desea ir Derecha(D) o Izquierda (I)")
opcion = opcion.upper()
if (opcion == 'D'):
    print('Caminas y de las palmeras caen arañas venenosas que te paralizan y colocan sus huevos dentro de tus orificios')
    print('FIN DEL JUEGO')
elif(opcion == 'I'):
    opcion_rio = input('Tienes un rio en frente ¿qué decides nadar(N) o esperar(E)')
    opcion_rio = opcion_rio.upper()
    if(opcion_rio == 'N'):
        print('Eres atacado por los cocodrilos que estaban ocultos\n FIN DEL JUEGO')
    elif(opcion_rio == 'E'):
        print('''
        El rio se seca de un momento a otro y entonces de ella emergen varias puertas hechas de roca\n
        Una es de color Roja, otra de color Azul y la ultima de Amarillo   
        ''')
        opcion_puerta = input("¿Cuál vas a escoger para entrar?  Roja(1), Azul (2), Amarrilla(3)")
        if(opcion_puerta == '1'):
            print('Quedaras atrapado en una dimensión infernal donde deberas luchar con miles de demonios por toda la eternidad')
        elif(opcion_puerta == '2'):
            print('Saldran muchas vestias salvajes y te devoraran')
        elif(opcion_puerta == '3'):
            print('Felicidades encontraste el tesoro. ¡haz ganado el juego!')
        else:
            print('Perdiste FIN DEL JUEGO por no decidir rapido')
    

