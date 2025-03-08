def suma(a, b):
    while b:
        carry = a & b  # Encuentra los bits que deben llevarse
        a = a ^ b  # Suma sin llevar
        b = carry << 1  # Se suma el carry
    return a

def resta(a, b):
    while b:
        borrow = (~a) & b  # Encuentra los bits que se deben tomar prestados
        a = a ^ b  # Resta sin borrow
        b = borrow << 1
    return a

def multiplicacion(a, b):
    resultado = 0
    while b:
        if b & 1:  # Si el bit menos significativo de b es 1
            resultado = suma(resultado, a)
        a <<= 1  # Multiplica por 2
        b >>= 1  # Divide entre 2
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

def main():
    while True:
        print("\nSeleccione la operación a realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '5':
            print("Saliendo...")
            break
        
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print("El resultado es:", suma(num1, num2))
        elif opcion == '2':
            print("El resultado es:", resta(num1, num2))
        elif opcion == '3':
            print("El resultado es:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("El resultado es:", division(num1, num2))
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
