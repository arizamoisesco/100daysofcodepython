print("Bienvenido a la calculadora del amor")
nombre1 = input("¿Cuál es su nombre?: ")
nombre2 = input("¿Cuál es el nombre de tu Crush?: ")

def calculo_amor(nombre, nombre2):
    #Combinemos los nombres para ser mas rapido en el conteo
    ustedes = nombre + nombre2
    ustedes = ustedes.lower()

    #Contar True primer nombre
    t = ustedes.count("t")
    r = ustedes.count("r")
    u = ustedes.count("u")
    e = ustedes.count("e")
    total_true = t+r+u+e

    #Contar Love primer nombre
    l = ustedes.count("l")
    o = ustedes.count("o")
    v = ustedes.count("v")
    e = ustedes.count("e")
    total_love = l+o+v+e
    
    #Convertimos los resultados de true y love en String para concatenarlos
    total_puntaje = str(total_true)+str(total_love)
    return total_puntaje


puntaje_amor = calculo_amor(nombre1, nombre2)
puntaje_amor = int(puntaje_amor)
if puntaje_amor < 10 or puntaje_amor > 90:
    print(f"Tu puntaje es {puntaje_amor}, vamos juntos por helado :(")
elif puntaje_amor > 40 and puntaje_amor < 50:
    print(f"Tu puntaje es {puntaje_amor}, estan bien juntos")
else:
    print(f"Tu puntaje es {puntaje_amor}")
