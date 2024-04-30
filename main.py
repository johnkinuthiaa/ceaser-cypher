alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction =input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shifting number: \n"))
shift =shift%25

# refactoring the ceasar code
def caesar(start_text,shift_amount, cypher_direction):
    end_text = ""
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)
            if cypher_direction == "encode":
                new_position = position + shift_amount
                end_text +=alphabet[new_position]
                shift_amount +=1
            else:
                new_position = position + shift_amount
                end_text +=alphabet[new_position]
                shift_amount -=1
        else:
            end_text +=i
    print(f"{cypher_direction}d text is {end_text}")
caesar(text,shift,direction)


