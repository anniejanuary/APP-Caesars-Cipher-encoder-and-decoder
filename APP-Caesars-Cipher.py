alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# 1: Combining the encrypt() and decrypt() functions into a single function called caesar().
def caesar (plain_text, encoded_text, shift_amount):
    
    # 'encrypt' function integrated into caesar() function (takes the 'text' and 'shift' as inputs)
    if direction == "encode":
        cipher_text = ""
        
        for letter in plain_text:    
            letter_index = alphabet.index(letter)
            
            # shifting each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
            new_letter_index = (letter_index + shift_amount) % 26
            # modulo for (letter_index + shift_amount) below 26: https://www.freecodecamp.org/news/content/images/2019/09/image-197.png
            # another expl: https://www.youtube.com/watch?v=Y6YTnkZ10qw
            
            new_letter = alphabet[new_letter_index]
            cipher_text += new_letter
        
        print(f"The encoded text is:\n{cipher_text}")
        
        
    # 'decrypt' function integrated into caesar() function (takes the 'text' and 'shift' as inputs)
    if direction == "decode":
        
        plain_text = ""
    
        #same as in encrypt function, but subtracting the shuft amount
        for letter in encoded_text:
            letter_index = alphabet.index(letter)
            new_letter_index = (letter_index - shift_amount) % 26
            new_letter = alphabet[new_letter_index]
            plain_text += new_letter
        
        print(f"The decoded text is:\n{plain_text}")

#BEFORE 1:
# Creating a function called 'encrypt' that takes the 'text' and 'shift' as inputs. 
# def encrypt (plain_text, shift_amount):
#     cipher_text = ""
#     
#     for letter in plain_text:    
#         letter_index = alphabet.index(letter)
#         
#         # shifting each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#         new_letter_index = (letter_index + shift_amount) % 26
#         # modulo for (letter_index + shift_amount) below 26: https://www.freecodecamp.org/news/content/images/2019/09/image-197.png
#         # another expl: https://www.youtube.com/watch?v=Y6YTnkZ10qw
#         
#         new_letter = alphabet[new_letter_index]
#         cipher_text += new_letter
#     
#     print(f"The encoded text is:\n{cipher_text}")
#     
# # function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt (encoded_text, shift_amount):
#     plain_text = ""
#     
#     #same as in encrypt function, but subtracting the shuft amount
#     for letter in encoded_text:
#         letter_index = alphabet.index(letter)
#         new_letter_index = (letter_index - shift_amount) % 26
#         new_letter = alphabet[new_letter_index]
#         plain_text += new_letter
#     
#     print(f"The decoded text is:\n{plain_text}")


#2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar (plain_text = text, encoded_text = text, shift_amount = shift)

# BEFORE 2:
#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt
#*AND* decrypt a message.

# if direction == "encode":
#     encrypt (plain_text = text, shift_amount = shift)
# elif direction == "decode":
#     decrypt (encoded_text = text, shift_amount = shift)
