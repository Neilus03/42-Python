import string
import sys
from sys import argv

def text_analyzer(txt = None):
    """
    Mi implementaci'on de la funci'on text_analyzer es capaz de contar la 
    cantidad de caracteres en un texto a la par que cuenta la cantidad de 
    mayúsculas, minúsculas espacios y signos de punntuación.
    
    Args:
		txt(str): texto a analizar.
    Retorna:
		None
    Raise:
        TypeError: si el argumento no es una string.
    """
    if txt is None:
        txt = input("Enter text: ")
    elif not isinstance(txt, str):
        raise TypeError("Not a string.")
        return
    upper_count, lower_count, space_count, punct_count, char_count = 0, 0, 0, 0, 0
    for char in txt:
        if char.isupper():
            upper_count+= 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punct_count += 1
        char_count += 1
    print ("The text contains", char_count, "character(s):\n-",upper_count, "upper letter(s)\n-", lower_count, "lower letter(s)\n-", punct_count, "punctuation mark(s)\n-", space_count, "space(s)")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Error: demasiados argumentos")
    else:
        text_analyzer(argv[1])