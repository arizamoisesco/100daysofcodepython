from art import logo

print(logo)
other_bid = True
all_bid = {}
max_value = 0
max_name = ""
while other_bid == True:
    name = input("Ingrese su nombre: ").capitalize()
    bid = int(input("Ingrese el precio de su oferta $"))
    all_bid[name] = bid
    question_bid = input("¿Otros usuarios van a ingresar alguna oferta? ").lower()
    if question_bid == "si":
        pass
    else:
        other_bid = False

print(all_bid)
for key, value in all_bid.items():
    if max_value < value:
        max_name = key
        max_value = value

print(f"El ganador es {max_name} con una oferta de ${max_value}")
