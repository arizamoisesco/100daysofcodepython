print("Bienvenido a Moises's Pizza")
tamaño = input("¿De que tamaño desea su pizza? G, M, P")

#Precios de las pizzas
pizza_pequeña = 15000
pizza_mediana = 20000
pizza_grande = 25000

def mensaje_costo(costo_pizza):
    '''
    Mensaje para despedir al usuario
    '''    
    print(f"Muchas gracias por su orden, su pedido estara listo en unos minutos, el costo de la pizza sera de ${costo_pizza}")

def pedir_queso(tamaño_pizza):
    queso_extra = input("¿Desea queso extra? S o N")
    if queso_extra == "S":
        tamaño_pizza +=1000
        mensaje_costo(tamaño_pizza)
    elif queso_extra == "N":
        mensaje_costo(tamaño_pizza)
    else:
        print("Opción incorrecta")

if tamaño == "G":
    agregar_peperoni = input("¿Desea agregar Peperoni S o N")
    if agregar_peperoni == "S":
        pizza_grande += 3000
        pedir_queso(pizza_grande)
        
elif tamaño == "M":
    agregar_peperoni = input("¿Desea agregar Peperoni S o N")
    if agregar_peperoni == "S":
        pizza_mediana += 3000
        pedir_queso(pizza_mediana)

elif tamaño == "P":
    agregar_peperoni = input("¿Desea agregar Peperoni S o N")
    if agregar_peperoni == "S":
        pizza_pequeña += 2000
        pedir_queso(pizza_pequeña)
else:
    print("Escogio una opción incorrecta")


        
    
        

