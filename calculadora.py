import sys
import tkinter as tk
from tkinter import messagebox

def suma(a, b):
    for _ in range(b):
        a += 1
    return a

def resta(a, b):
    for _ in range(b):
        a -= 1
    return a

def multiplicacion(a, b):
    resultado = 0
    negativo = False
    
    if b < 0:
        b = resta(0, b)
        negativo = not negativo
    if a < 0:
        a = resta(0, a)
        negativo = not negativo
    
    for _ in range(b):
        resultado = suma(resultado, a)
    
    return resta(0, resultado) if negativo else resultado

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    resultado = 0
    negativo = False
    
    if b < 0:
        b = resta(0, b)
        negativo = not negativo
    if a < 0:
        a = resta(0, a)
        negativo = not negativo
    
    while a >= b:
        a = resta(a, b)
        resultado = suma(resultado, 1)
    
    return resta(0, resultado) if negativo else resultado

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

operaciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division,
    "potencia": potencia,
    "factorial": factorial,
    "raiz_cuadrada": raiz_cuadrada
}

def calcular(operacion, num1, num2=None):
    if operacion in operaciones:
        return operaciones[operacion](num1, num2) if num2 is not None else operaciones[operacion](num1)
    return "Operación no válida"

def interfaz_grafica():
    def ejecutar_calculo(operacion):
        try:
            num1 = int(entry_num1.get())
            num2 = int(entry_num2.get()) if operacion not in ["factorial", "raiz_cuadrada"] else None
            resultado = calcular(operacion, num1, num2)
            label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    root = tk.Tk()
    root.title("Calculadora Sin Operadores")
    root.geometry("500x350")

    frame_entrada = tk.Frame(root)
    frame_entrada.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(frame_entrada, text="Ingrese el primer número:").pack()
    entry_num1 = tk.Entry(frame_entrada)
    entry_num1.pack()

    tk.Label(frame_entrada, text="Ingrese el segundo número (si aplica):").pack()
    entry_num2 = tk.Entry(frame_entrada)
    entry_num2.pack()

    for op in operaciones.keys():
        tk.Button(frame_entrada, text=op.capitalize(), command=lambda o=op: ejecutar_calculo(o)).pack()

    frame_resultado = tk.Frame(root)
    frame_resultado.pack(side=tk.RIGHT, padx=20, pady=20)

    label_resultado = tk.Label(frame_resultado, text="Resultado: ", font=("Arial", 14))
    label_resultado.pack()

    tk.Button(frame_resultado, text="Salir", command=root.quit).pack()
    root.mainloop()

def modo_consola():
    while True:
        sys.stdout.write("Seleccione operación (suma, resta, multiplicacion, division, potencia, factorial, raiz_cuadrada) o 'salir' para terminar:\n")
        sys.stdout.flush()
        operacion = sys.stdin.readline().strip()
        if operacion == "salir":
            break
        
        sys.stdout.write("Ingrese el primer número:\n")
        sys.stdout.flush()
        num1 = int(sys.stdin.readline().strip())

        num2 = None
        if operacion not in ["factorial", "raiz_cuadrada"]:
            sys.stdout.write("Ingrese el segundo número:\n")
            sys.stdout.flush()
            num2 = int(sys.stdin.readline().strip())

        resultado = calcular(operacion, num1, num2)
        sys.stdout.write(f"El resultado es: {resultado}\n")
        sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        modo_consola()
    else:
        interfaz_grafica()
