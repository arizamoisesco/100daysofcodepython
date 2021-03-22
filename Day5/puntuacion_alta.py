puntuacion_estudiante = input("Ingrese la lista de puntaje de los estudiantes ").split()
for n in range(0 , len(puntuacion_estudiante)):
    puntuacion_estudiante[n] = int(puntuacion_estudiante[n])

#Crear el bucle
#Dentro del bucle comparar número por número 
#Si el número que viene es mayor que el que se guarda 
#Entonces lo reemplazo
numero_maximo = 0
for puntuacion in puntuacion_estudiante:
    if(puntuacion > numero_maximo):
        numero_maximo = puntuacion

print(f"La puntuación mas alta en la clase fue: {numero_maximo}")