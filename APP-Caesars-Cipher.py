alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Creating a function called 'encrypt' that takes the 'text' and 'shift' as inputs. 
def encrypt (plain_text, shift_amount):
    cipher_text = "" # needs to be declared above the for loop, otherwise append wouldn't work. Each new_letter would replace the previous one
    
    for letter in plain_text:    
        letter_index = alphabet.index(letter)
        
        # shifting each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
        new_letter_index = (letter_index + shift_amount) % 26
        # modulo for (letter_index + shift_amount) below 26: https://www.freecodecamp.org/news/content/images/2019/09/image-197.png
        # another expl: https://www.youtube.com/watch?v=Y6YTnkZ10qw
        
        new_letter = alphabet[new_letter_index]
        cipher_text += new_letter
    
    print(f"The encoded text is:\n{cipher_text}")

encrypt(text, shift)
