import sys
from sys import argv

# Función para invertir y cambiar mayúsculas a minúsculas y viceversa
def invertir_cambiar(string):
    # Invertir el string
    string = string[::-1]
    # Cambiar mayúsculas a minúsculas y viceversa
    string = string.swapcase()
    return string

# Obtener los argumentos de la línea de comandos
args = argv[1:]

# Verificar si se proporcionó algún argumento
if not args:
    print("El programa requiere al menos un argumento.")

else:
    # Combinar los argumentos en un solo string separados por un espacio
	string = ' '.join(args)
    # Aplicar la función a la cadena combinada
	resultado = invertir_cambiar(string)
    # Imprimir el resultado
	print(resultado)
