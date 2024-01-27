#In the caesar cipher, you will take each letter in your message, find its position in the alphabet,
#take the letter located after 3 positions,
#and replace the original letter with the new letter.
#For example the plain text "Hello" will be encrypted in "Khoor".
text = 'Hello my name is Yannick'
shift = 3

def vigenere(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
	#To avoid a blank space to be encrypted
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

vigenere(text,shift)
