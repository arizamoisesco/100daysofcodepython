print("Bienvenido a la calculadora del amor")
nombre1 = input("¿Cuál es su nombre?: ")
nombre1 = nombre1.lower()
nombre2 = input("¿Cuál es su nombre?: ")
nombre2 = nombre2.lower()

def calculo_amor(nombre, nombre2):
    #Contar True primer nombre
    t = nombre.count("t")
    r = nombre.count("r")
    u = nombre.count("u")
    e = nombre.count("e")
    nombre1_true = t+r+u+e

    #Contar True segundo nombre
    t = nombre.count("t")
    r = nombre.count("r")
    u = nombre.count("u")
    e = nombre.count("e")
    nombre2_true = t+r+u+e

    total_true = str(nombre1_true + nombre2_true)
    #Contar Love primer nombre
    l = nombre.count("l")
    o = nombre.count("o")
    v = nombre.count("v")
    e = nombre.count("e")
    nombre1_love = l+o+v+e

    #Contar Love segundo nombre
    l = nombre.count("l")
    o = nombre.count("o")
    v = nombre.count("v")
    e = nombre.count("e")
    nombre2_love = l+o+v+e

    total_love = str(nombre1_love + nombre2_love)
    
    total = int(total_true+total_love)
    return total

'''
total_nombre1 = calculo_amor(nombre1)
print(total_nombre1)
total_nombre2 = calculo_amor(nombre2)
print(total_nombre2)
'''

puntaje_amor = calculo_amor(nombre1, nombre2)

if puntaje_amor < 10 or puntaje_amor > 90:
    print(f"Tu puntaje es {puntaje_amor}, vamos juntos por helado :(")
elif puntaje_amor > 40 and puntaje_amor < 50:
    print(f"Tu puntaje es {puntaje_amor}, estan bien juntos")
else:
    print(f"Tu puntaje es {puntaje_amor}")
