
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
option_continue = "s"
     
num1 = int(input("¿Cual es el primer número?: "))
num2 = int(input("¿Cual es el segundo número?: "))
print("¿Qué operación desea realizar?: ")
for key in operations:
    print(key)
operation_symbol = input("Ingrese el simbolo de la operación que desea realizar: ")

select_operation = operations[operation_symbol]
first_answer = select_operation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
num3 = int(input("¿Cuál es el siguiente numero"))
operation_symbol = input("Escriba la siguiente operacion: ").lower()
select_operation = operations[operation_symbol]
second_answer = select_operation(select_operation(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")