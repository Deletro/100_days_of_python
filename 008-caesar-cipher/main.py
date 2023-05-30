# fmt: off
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# fmt: on


def caesar(text, shift, direction):
    text_holder = ""
    for letter in text:
        if letter not in alphabet:
            text_holder += letter
            continue
        ori_index = alphabet.index(letter)
        if direction == "encode":
            new_index = ori_index + shift
        elif direction == "decode":
            new_index = ori_index - shift
        else:
            print(f"'{direction}' data entry error")
            return
        new_index = new_index % len(alphabet)
        text_holder += alphabet[new_index]
    print(text_holder)


user_input = "yes"
while user_input == "yes":
    direction = input("Type 'encode' encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_input = input("Do you wish to countinue?: 'yes' or 'no'\n")
