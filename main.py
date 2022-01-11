alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# se define la funcion cesar que encript o desencripta
def caesar(plain_text, shift_amount, arrow):
    cipher_text = ""

    if arrow == "decode":
        shift_amount *= -1

    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    # f strings mas el valor decode o encode de arrow
    print(f"The {arrow}d text is {cipher_text}")


# se termina la funcion
# se define el fin del script

end_of_script = False

# define ciclo while para que se siga ejecutando
while end_of_script == False:
    # pide los datos de la encriptacion
    direction = input("Type 'encode' to encrypt, type   'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # ejecuta la funcion
    caesar(plain_text=text, arrow=direction, shift_amount=shift)
    # reinicia?
    restart = input("restart? input Y or N \n").upper()

    if restart == "N":
        end_of_script = True
    else:
        end_of_script = False