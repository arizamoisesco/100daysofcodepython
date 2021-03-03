print("Bienvenido a Moises's Pizza")
tamaño = input("¿De que tamaño desea su pizza? G, M, P")
agregar_peperoni = input("¿Desea agregar Peperoni S o N")

#Precios de las pizzas
pizza_pequeña = 15000
pizza_mediana = 20000
pizza_grande = 25000

if tamaño == "G":
    agregar_peperoni = input("¿Desea agregar Peperoni S o N")
    if agregar_peperoni == "S":
        pizza_grande += 3000
elif tamaño == "M":
    agregar_peperoni = input("¿Desea agregar Peperoni S o N")
    if agregar_peperoni == "S":
        pizza_mediana += 3000
elif tamaño == "P":
    agregar_peperoni = input("¿Desea agregar Peperoni S o N")
    if agregar_peperoni == "S":
        pizza_pequeña += 2000
else:
    print("Escogio una opción incorrecta")

queso_extra = input("¿Desea queso extra? S o N")


