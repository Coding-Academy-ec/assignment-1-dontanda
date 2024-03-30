"""
Este programa sirve para realizar las cuatro operaciones básicas (suma, resta,
multiplicación, división) con dos números ingresados por el usuario.
"""

# Suma de dos numeros
def sumar(a, b):
    return a + b

# Resta de dos numeros
def restar(a, b):
    return a - b

# Multiplicacion de dos numeros
def multiplicar(a, b):
    return a * b

# Division de dos numeros
def dividir(a, b):
    if ( b == 0 ):
        return "No se puede dividir para cero"
    return a / b


def main():
    num1 = float(input("Escriba el primer número: "))
    num2 = float(input("Escriba el segundo número: "))

    print("Suma:", sumar(num1, num2))
    print("Resta:", restar(num1, num2))
    print("Multiplicación:", multiplicar(num1, num2))
    print("División:", dividir(num1, num2))

if __name__ == "__main__":
    main()