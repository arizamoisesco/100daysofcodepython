
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

num1 = int(input("¿Cual es el primer número?: "))
num2 = int(input("¿Cual es el segundo número?: "))
print("¿Qué operación desea realizar?: ")
for key in operations:
    print(key)
operation_symbol = input("Ingrese el simbolo de la operación que desea ralizar: ")

select_operation = operations[operation_symbol]
answer = select_operation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")