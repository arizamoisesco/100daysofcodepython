from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Dictionary 
operations = {"+":add,
             "-":subtract,
             "*":multiply,
             "/":divide
}

def calculator():    
    print(logo)

    num1 = float(input("¿Cual es el primer número?: "))

    print("¿Qué operación desea realizar?: ")
    for key in operations:
        print(key)

    option_continue = True

    while option_continue:
        operation_symbol = input("Ingrese el simbolo de la operación que desea realizar: ")

        num2 = float(input("¿Cual es el siguiente número?: "))

        select_operation = operations[operation_symbol]
        answer = select_operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Escribe 'y' para continuar calculando con la {answer}, o escribe 'n' para iniciar un nuevo calculo: ") == 'y':
            num1 = answer 
        else:
            option_continue = False
            calculator()

calculator()

