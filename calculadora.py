import sys
import tkinter as tk
from tkinter import messagebox

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

def calcular(operacion):
    try:
        num1 = int(entry_num1.get())
        if operacion in ["factorial", "raiz_cuadrada"]:
            resultado = factorial(num1) if operacion == "factorial" else raiz_cuadrada(num1)
        else:
            num2 = int(entry_num2.get())
            if operacion == "suma":
                resultado = suma(num1, num2)
            elif operacion == "resta":
                resultado = resta(num1, num2)
            elif operacion == "multiplicacion":
                resultado = multiplicacion(num1, num2)
            elif operacion == "division":
                resultado = division(num1, num2)
            elif operacion == "potencia":
                resultado = potencia(num1, num2)
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Sin Operadores")
root.geometry("500x350")

frame_entrada = tk.Frame(root)
frame_entrada.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(frame_entrada, text="Ingrese el primer número:").pack()
entry_num1 = tk.Entry(frame_entrada)
entry_num1.pack()

tk.Label(frame_entrada, text="Ingrese el segundo número:").pack()
entry_num2 = tk.Entry(frame_entrada)
entry_num2.pack()

tk.Button(frame_entrada, text="Suma", command=lambda: calcular("suma")).pack()
tk.Button(frame_entrada, text="Resta", command=lambda: calcular("resta")).pack()
tk.Button(frame_entrada, text="Multiplicación", command=lambda: calcular("multiplicacion")).pack()
tk.Button(frame_entrada, text="División", command=lambda: calcular("division")).pack()
tk.Button(frame_entrada, text="Potencia", command=lambda: calcular("potencia")).pack()
tk.Button(frame_entrada, text="Factorial", command=lambda: calcular("factorial")).pack()
tk.Button(frame_entrada, text="Raíz Cuadrada", command=lambda: calcular("raiz_cuadrada")).pack()

frame_resultado = tk.Frame(root)
frame_resultado.pack(side=tk.RIGHT, padx=20, pady=20)

label_resultado = tk.Label(frame_resultado, text="Resultado: ", font=("Arial", 14))
label_resultado.pack()

tk.Button(frame_resultado, text="Salir", command=root.quit).pack()

root.mainloop()


