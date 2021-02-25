#Calculadora de propinas
#Ponemos el mensaje de bienvenida 
print("Hola y bienenido a la calculadora de propinas\n")
#Pedimos el total de la cuenta
total_cuenta = int(input("Ingrese el total de la cuenta: \n"))
#Entre cuantas personas se va a repartir 
cantidad_personas = int(input("¿Entre cuantas personas se va a dividir la cuenta?: \n"))
#Determinamos el porcentaje de la cuenta a pagar 
porcentaje_propina = int(input("¿cuál es el porcentaje de propina que desea pagar? ¿10, 12 o 15? \n"))

#Operación
#Dividimos la cuenta 
resultado = total_cuenta / cantidad_personas
propina = (resultado * porcentaje_propina)/100
pago_final = round(resultado + propina, 2)

#Resultado 
print(f"Debe pagar ${pago_final}")
