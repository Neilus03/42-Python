from sys import argv

def operations(A, B):
    print("Sum:", A+B)
    print("Difference:", A-B)
    print("Product:", A*B)
    print("Quotient:", A/B) if B != 0 else print("Quotient: ERROR(Zero Division Error)")
    print("Reminder:", A%B) if B != 0 else print("Reminder: ERROR(Modulo by zero Error)")

try:
    args = argv[1:]
    if len(args) != 2:
        raise AssertionError("AssertionError: El programa requiere de 2 argumentos.")
    else:
        try:
            int(args[0]) and int(args[1])
            operations(int(args[0]), int(args[1]))
        except ValueError:
            raise AssertionError("AssertionError: El argumento debe ser un número entero.")
except Exception as exception:
    print(exception)
          

    
