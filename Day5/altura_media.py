altura_estudiantes = input("Ingrese la lista de peso de altura de sus estudiantes ").split()
for n in range(0, len(altura_estudiantes)):
    altura_estudiantes[n] = int(altura_estudiantes[n])

cantidad_alturas = 0
total_altura = 0
#Sumar los valores que esten dentro de lista de estudiantes y determinar cuantos son
for i in altura_estudiantes:
    print(cantidad_alturas)
    total_altura += i 
    cantidad_alturas += 1

#Dividirlos entre si ysacar la media 
altura_media = total_altura / cantidad_alturas
print("*****")
print(f"La altura media del grupo es: {round(altura_media)}")
print(total_altura)
print(cantidad_alturas)
