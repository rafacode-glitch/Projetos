import tkinter as tk


def encontrar_multiplos():
    numero = int(numero_entry.get())
    inicio_intervalo = int(inicio_entry.get())
    fim_intervalo = int(fim_entry.get())

    numeros = range(inicio_intervalo, fim_intervalo+1, numero)

    output_text.delete(1.0, tk.END)
    for numero in numeros:
        output_text.insert(tk.END, f"{numero}\n")


# Cria a janela principal
janela = tk.Tk()
janela.title("Encontrar Múltiplos")

# Cria os widgets da interface
tk.Label(janela, text="Número:").pack()
numero_entry = tk.Entry(janela)
numero_entry.pack()

tk.Label(janela, text="Início do Intervalo:").pack()
inicio_entry = tk.Entry(janela)
inicio_entry.pack()

tk.Label(janela, text="Fim do Intervalo:").pack()
fim_entry = tk.Entry(janela)
fim_entry.pack()

tk.Button(janela, text="Encontrar Múltiplos",
          command=encontrar_multiplos).pack()

output_text = tk.Text(janela, height=10, width=30)
output_text.pack()

# Inicia o loop de eventos da interface gráfica
janela.mainloop()
