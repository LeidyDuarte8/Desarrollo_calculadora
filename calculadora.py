def suma(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def resta(a, b):
    while b:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

def multiplicacion(a, b):
    resultado = 0
    while b:
        if b & 1:
            resultado = suma(resultado, a)
        a <<= 1
        b >>= 1
    return resultado

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    cociente = 0
    while a >= b:
        temp_b = b
        multiplicador = 1
        while (temp_b << 1) <= a:
            temp_b <<= 1
            multiplicador <<= 1
        a = resta(a, temp_b)
        cociente = suma(cociente, multiplicador)
    return cociente

def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    while n > 1:
        resultado = multiplicacion(resultado, n)
        n = resta(n, 1)
    return resultado

def potencia(base, exponente):
    resultado = 1
    while exponente > 0:
        resultado = multiplicacion(resultado, base)
        exponente = resta(exponente, 1)
    return resultado

def raiz_cuadrada(n):
    if n < 0:
        return "Error: Número negativo"
    x = n
    y = 1
    while x > y:
        x = division(suma(x, y), 2)
        y = division(n, x)
    return x

# Diccionario de operaciones para permitir expansión fácil
operaciones = {
    "1": ("Suma", suma, True),
    "2": ("Resta", resta, True),
    "3": ("Multiplicación", multiplicacion, True),
    "4": ("División", division, True),
    "5": ("Factorial", factorial, False),
    "6": ("Potencia", potencia, True),
    "7": ("Raíz Cuadrada", raiz_cuadrada, False),
    "8": ("Salir", None, False),
}

def main():
    while True:
        print("\nSeleccione la operación a realizar:")
        for key, (nombre, _, requiere_segundo) in operaciones.items():
            print(f"{key}. {nombre}")

        opcion = input("Ingrese una opción: ")
        if opcion == "8":
            print("Saliendo...")
            break

        if opcion not in operaciones:
            print("Opción no válida, intente de nuevo.")
            continue

        num1 = int(input("Ingrese el primer número: "))
        if operaciones[opcion][2]:  # Si la operación requiere segundo número
            num2 = int(input("Ingrese el segundo número: "))
            resultado = operaciones[opcion][1](num1, num2)
        else:
            resultado = operaciones[opcion][1](num1)

        print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()
