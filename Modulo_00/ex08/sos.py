import sys

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': '/'
}

def encode_morse(text):
    encoded = []
    for char in text:
        if char.upper() in MORSE_CODE:
            encoded.append(MORSE_CODE[char.upper()])
        else:
            return "ERROR"
    return ' '.join(encoded)

if len(sys.argv) == 1:
    print("Usage: python3 sos.py 'text to encode'")
else:
    message = ' '.join(sys.argv[1:])
    encoded_message = encode_morse(message)
    print(encoded_message)
