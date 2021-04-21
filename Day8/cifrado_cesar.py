alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
    text_plan = ""
    position_alphabet = 0
    len_alphabet = len(alphabet)-1
    for letter in text:
        if direction == "encode":
            position_alphabet  = alphabet.index(letter) + shift
        elif direction == "decode":
            position_alphabet  = alphabet.index(letter) - shift
    
        if position_alphabet > len_alphabet:
            position_alphabet = 0

        text_plan += alphabet[position_alphabet]
    print(f"The message {direction}d is {text_plan}")

ceaser(text, shift, direction)

  