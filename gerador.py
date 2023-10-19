import random
import tkinter as tk
from tkinter import messagebox

def gerar_numeros_loteria():
    jogo = escolha_var.get()

    if jogo == 1:
        sorteio = random.sample(range(1, 60), 6)
        sorteio.sort()
        resultado_label.config(text=f"Os números aleatórios da Mega-Sena são: {sorteio}")
    elif jogo == 2:
        sorteio = random.sample(range(1, 25), 15)
        sorteio.sort()
        resultado_label.config(text=f"Os números aleatórios da Lotofacil são: {sorteio}")
    elif jogo == 3:
        sorteio = random.sample(range(1, 80), 5)
        sorteio.sort()
        resultado_label.config(text=f"Os números aleatórios da Quina são: {sorteio}")

def verificar_opcao():
    verificacao = messagebox.askyesno("Confirmação", "Você tem certeza que deseja essa opção?")
    if verificacao:
        gerar_numeros_loteria()

def reiniciar():
    resultado_label.config(text="")
    escolha_var.set(0)

app = tk.Tk()
app.title("Gerador de Números da Loteria")

escolha_label = tk.Label(app, text="Escolha o jogo da Loteria:")
escolha_label.pack()

escolha_var = tk.IntVar()
escolha_var.set(0)

mega_sena_radio = tk.Radiobutton(app, text="Mega-Sena", variable=escolha_var, value=1)
lotofacil_radio = tk.Radiobutton(app, text="Lotofacil", variable=escolha_var, value=2)
quina_radio = tk.Radiobutton(app, text="Quina", variable=escolha_var, value=3)

mega_sena_radio.pack()
lotofacil_radio.pack()
quina_radio.pack()

gerar_button = tk.Button(app, text="Gerar Números", command=verificar_opcao)
gerar_button.pack()

resultado_label = tk.Label(app, text="")
resultado_label.pack()

reiniciar_button = tk.Button(app, text="Reiniciar", command=reiniciar)
reiniciar_button.pack()

app.mainloop()
