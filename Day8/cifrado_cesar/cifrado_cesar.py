import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift, direction):
    text_plan = ""
    position_alphabet = 0
    len_alphabet = len(alphabet)-1
    for char in text:
        if direction == "encode":
            if char in alphabet:
                position_alphabet  = alphabet.index(char) + shift

        elif direction == "decode":
            if char in alphabet:
                position_alphabet  = alphabet.index(char) - shift
    
        if position_alphabet > len_alphabet:
            position_alphabet = 0

        if char in alphabet:
            text_plan += alphabet[position_alphabet]
        else:
            text_plan += char
    print(f"The message {direction}d is {text_plan}")

option_continue = "yes"
while(option_continue == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)
    option_continue = input("Are you want continue yes or no?")

print("Thanks for used me")

    