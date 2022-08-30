alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1: Combining the encrypt() and decrypt() functions into a single function called caesar().
def caesar (start_text, shift_amount, cipher_direction): # before I tried: def caesar (plain_text, encoded_text, shift_amount) AND IT WORKED JUST FINE, TOO
                                                         # -> but no need to different. text type, it's just a starting text. Also task said: include direction.
                                                         # I call these (parameters) whatever I want, doesnt matter, I just need to call the function with (arguments) later / the actual value. OR: (parameter = argument)
        
    # BEFORE i had >>cipher_text = ""<< here, same as >>plain_text = ""<< below. now to simplify I just have >>end_text = ""<<
    end_text = ""
    
    for char in start_text:    #BEFORE combining encode and decode functions I differentiated between "plain_text" and "encoded_text", no need for that now in the spirit of simplification
        if char in alphabet:
            letter_index = alphabet.index(char)
        
            # 'encrypt' function integrated into caesar() function (takes the 'text' and 'shift' as inputs)
            if cipher_direction == "encode":
                # shifting each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
                new_letter_index = (letter_index + shift_amount) % 26
                # modulo for (letter_index + shift_amount) below 26: https://www.freecodecamp.org/news/content/images/2019/09/image-197.png
                # another expl: https://www.youtube.com/watch?v=Y6YTnkZ10qw
                
            # 'decrypt' function integrated into caesar() function (takes the 'text' and 'shift' as inputs)    
            if cipher_direction == "decode":
                #same as in encrypt function, but subtracting the shuft amount
                new_letter_index = (letter_index - shift_amount) % 26  # ANOTHER WAY, MOVING IT OUTSIDE OF THE FORLOOP: (so that shift_amount doesn't get looped and mangled : 1. loop: shift_amount: eg. 5 * -1 = -5 || 2. loop: -5 * -1 = 5 etc. so that consecutive letters are encoded in diff directions in the alphabet
                                                                       # if cipher_direction == "decode": || shift_amount *= -1  -> switches to substraction
            new_letter = alphabet[new_letter_index]
            end_text += new_letter    # BEFORE it was cipher_text in encode function or plain_text in decode function instead of end_text
        
        
        #the number/symbol/space when the text is encoded/decoded? #e.g. start_text = "meet me at 3" #end_text = "•••• •• •• 3"
        else:
            end_text += char
    
    print(f"The {cipher_direction}d text is:\n{end_text}")    # BEFORE it was cipher_text in encode f. and plain_text in decode f. instead of end_text
 
# 3: Importing and printing the logo from ascii_art.py when the program starts
import ascii_art  #🔀 from ascii_art import logo
print(ascii_art.logo)


# 4: asking the user if they want to restart the cipher program

continue_cipher = True

while continue_cipher: # implied that continue == True
     
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
      
    # 2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar (start_text = text, shift_amount = shift, cipher_direction = direction)

    decision = input("Would you like to play again? Type 'yes' or 'no': \n")
    if decision == "no":
        continue_cipher = False
        print("Bye!")



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

# BEFORE 2:
#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt
#*AND* decrypt a message.

# if direction == "encode":
#     encrypt (plain_text = text, shift_amount = shift)
# elif direction == "decode":
#     decrypt (encoded_text = text, shift_amount = shift)
