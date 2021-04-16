import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    #Sin el math.ceil no se redondearia al maximo por eso es más práctico para este caso que 
    #Usar la función round
    resultado = math.ceil((height * width)/cover)
    print(f"Tu necesitas {resultado} botes de pintura")

paint_calc(height=test_h, width=test_w, cover=coverage)

