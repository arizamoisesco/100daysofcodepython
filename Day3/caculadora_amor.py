print("Bienvenido a la calculadora del amor")
nombre1 = input("¿Cuál es su nombre?: ")
nombre1 = nombre1.lower()
nombre2 = input("¿Cuál es su nombre?: ")
nombre2 = nombre2.lower()

def calculo_amor(nombre):
    #Contar True
    t = nombre.count("t")
    r = nombre.count("r")
    u = nombre.count("u")
    e = nombre.count("e")
    #Contar Love
    l = nombre.count("l")
    o = nombre.count("o")
    v = nombre.count("v")
    e = nombre.count("e")
    
    total = t+r+u+e+l+o+v+e
    return total

total_nombre1 = calculo_amor(nombre1)
print(total_nombre1)
total_nombre2 = calculo_amor(nombre2)
print(total_nombre2)

puntaje_amor = total_nombre1 + total_nombre2

if puntaje_amor < 10 or puntaje_amor > 90:
    print(f"Tu puntaje es {puntaje_amor}, vamos juntos por helado :(")
elif puntaje_amor > 40 and puntaje_amor < 50:
    print(f"Tu puntaje es {puntaje_amor}, estan bien juntos")
else:
    print(f"Tu puntaje es {puntaje_amor}")
