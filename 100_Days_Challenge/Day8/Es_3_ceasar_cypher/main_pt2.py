#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
  #amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  
  
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#Then call the correct function based on that 'drection' variable.
#You should be able to test the code to encrypt *AND* decrypt a message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encryptedWord = ""
    shiftedLetter = ""
        
    for index in range(0, len(text)):
        
        #check if the char in the string is a symbol or a letter
        if(text[index] in alphabet):
            #Check the boundary of the list, if we go out of bounds wrap around to the start of the list
            if((alphabet.index(text[index]) + shift) > len(alphabet) - 1):
                shiftedLetter = alphabet[(alphabet.index(text[index]) + shift - len(alphabet))]
            else:
                shiftedLetter = alphabet[(alphabet.index(text[index]) + shift)]
            
            encryptedWord = encryptedWord + shiftedLetter
        else:
            encryptedWord = encryptedWord + text[index]
    
    print(f"The encoded text is: {encryptedWord}")
    
def decrypt(text, shift):
    decryptedWord = ""
    shiftedLetter = ""
    for index in range(0, len(text)):
        
        #check if the char in the string is a symbol or a letter
        if(text[index] in alphabet):
            shiftedLetter = alphabet[(alphabet.index(text[index]) - shift)]
            decryptedWord = decryptedWord + shiftedLetter
        else:
            decryptedWord = decryptedWord + text[index]
    print(f"The decrypted word is: {decryptedWord}")
    
exitFlag = 0

while(not exitFlag):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, anything else to exit:\n")
    if(direction == "encode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif(direction == "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        exitFlag = 1
    
     