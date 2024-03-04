import tkinter as tk
from tkinter import messagebox

# Define as cores do tema claro e escuro
cor_fundo_claro = "white"
cor_texto_claro = "black"
cor_fundo_escuro = "black"
cor_texto_escuro = "white"

# Define o estado inicial do tema como claro
tema_escuro = False


def alternar_tema():
    global tema_escuro
    if tema_escuro:
        tema_escuro = False
        janela.config(bg=cor_fundo_claro)
        for widget in janela.winfo_children():
            widget.config(bg=cor_fundo_claro, fg=cor_texto_claro)
    else:
        tema_escuro = True
        janela.config(bg=cor_fundo_escuro)
        for widget in janela.winfo_children():
            widget.config(bg=cor_fundo_escuro, fg=cor_texto_escuro)


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
janela.config(bg=cor_fundo_claro)

# Cria os widgets da interface
tk.Label(janela, text="Número:", bg=cor_fundo_claro, fg=cor_texto_claro).pack()
numero_entry = tk.Entry(janela)
numero_entry.pack()

tk.Label(janela, text="Início do Intervalo:",
         bg=cor_fundo_claro, fg=cor_texto_claro).pack()
inicio_entry = tk.Entry(janela)
inicio_entry.pack()

tk.Label(janela, text="Fim do Intervalo:",
         bg=cor_fundo_claro, fg=cor_texto_claro).pack()
fim_entry = tk.Entry(janela)
fim_entry.pack()

tk.Button(janela, text="Encontrar Múltiplos", command=encontrar_multiplos,
          bg=cor_fundo_claro, fg=cor_texto_claro).pack()
tk.Button(janela, text="Alternar Tema", command=alternar_tema,
          bg=cor_fundo_claro, fg=cor_texto_claro).pack()

output_text = tk.Text(janela, height=10, width=30,
                      bg=cor_fundo_claro, fg=cor_texto_claro)
output_text.pack()

# Inicia o loop de eventos da interface gráfica
janela.mainloop()
