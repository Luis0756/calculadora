import tkinter as tk
from tkinter import messagebox

def f(x):
    return x**3 - 4*x + 1

def bisseccao(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        messagebox.showerror("Erro", "f(a) e f(b) devem ter sinais opostos.")
        return None

    iteracoes = 0
    while (b - a) / 2.0 > tol and iteracoes < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteracoes += 1

    return (a + b) / 2.0

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        tol = float(entry_tol.get())
        raiz = bisseccao(a, b, tol)

        if raiz is not None:
            resultado_label.config(text=f"Raiz aproximada: {raiz:.6f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

janela = tk.Tk()
janela.title("Método da Bissecção")
janela.geometry("300x250")

tk.Label(janela, text="Limite inferior (a):").pack()
entry_a = tk.Entry(janela)
entry_a.pack()

tk.Label(janela, text="Limite superior (b):").pack()
entry_b = tk.Entry(janela)
entry_b.pack()

tk.Label(janela, text="Tolerância:").pack()
entry_tol = tk.Entry(janela)
entry_tol.pack()

btn = tk.Button(janela, text="Calcular", command=calcular)
btn.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()
