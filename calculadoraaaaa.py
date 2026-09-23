import tkinter as tk


def agregar(valor):
	pantalla.insert(tk.END, valor)


def limpiar():
	pantalla.delete(0, tk.END)


def calcular():
	try:
		expresion = pantalla.get().replace("×", "*").replace("÷", "/")
		resultado = eval(expresion, {"__builtins__": {}}, {})
		pantalla.delete(0, tk.END)
		pantalla.insert(0, str(resultado))
	except (SyntaxError, ZeroDivisionError, TypeError, ValueError):
		pantalla.delete(0, tk.END)
		pantalla.insert(0, "Error")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.resizable(False, False)

pantalla = tk.Entry(ventana, width=18, font=("Arial", 24), justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

botones = [
	("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
	("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
	("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
	("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for texto, fila, columna in botones:
	comando = calcular if texto == "=" else lambda valor=texto: agregar(valor)
	tk.Button(
		ventana, text=texto, command=comando, width=5, height=2,
		font=("Arial", 14)
	).grid(row=fila, column=columna, padx=3, pady=3)

tk.Button(
	ventana, text="Limpiar", command=limpiar, width=23, height=2,
	font=("Arial", 12)
).grid(row=5, column=0, columnspan=4, padx=3, pady=5)

ventana.mainloop()
