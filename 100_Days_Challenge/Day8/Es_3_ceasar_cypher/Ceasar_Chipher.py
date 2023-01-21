alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
exitFlag = 0

def ceasar(direction, text, shift):
    shiftedLetter = ""
    newWord = ""
    ALPHABET_LENGTH = len(alphabet)
    TEXT_LENGTH = len(text)
    shift = shift % ALPHABET_LENGTH
     
    if(direction == "decode"):
        shift *= -1
    
    for index in range(0, TEXT_LENGTH):
        if(text[index] in alphabet):
            #Check the boundary of the list, if we go out of bounds wrap around to the start of the list
            if((alphabet.index(text[index]) + shift) > ALPHABET_LENGTH - 1):
                shiftedLetter = alphabet[(alphabet.index(text[index]) + shift - ALPHABET_LENGTH)]
            else:
                shiftedLetter = alphabet[(alphabet.index(text[index]) + shift)]
            
            newWord = newWord + shiftedLetter
        else:
            newWord = newWord + text[index] 
    
    print(f"The decrypted word is: {newWord}\n")

while(not exitFlag):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, anything else to exit:\n").lower()
    if(direction != "encode" and direction != "decode"):
        exitFlag = 1
        print("\nGoodbye!\n")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceasar(direction, text, shift)
        
