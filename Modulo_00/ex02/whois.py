import sys
from sys import argv

def check(n):
    if n == 0:
        print("El número es cero.")
    elif n % 2 == 0:
        print("El número es par.")
    else:
         print("El número es impar.")

if len(argv) < 2:
      raise AssertionError("No hay argumentos que verificar")
elif len(argv) > 2:
	raise AssertionError("Demasiados argumentos para verificar.")
else:
	try:
		arg = int(argv[1])
		check(arg)
	except ValueError:
		raise AssertionError("El argumento debe ser un número entero.")
