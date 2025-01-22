# Importação da biblioteca tkinter para criar interfaces gráficas
import tkinter as tk
from tkinter import Label, Frame, Entry, Button

# Função para calcular o IMC (Índice de Massa Corporal)
def calcula_imc():
    # Calcula o IMC usando o peso e altura fornecidos
    imc = float(peso.get()) / float(altura.get()) ** 2
    # Atualiza o texto do Label com o resultado do IMC
    resultado['text'] = f'O seu IMC é {imc:.2f}'

# Cria a janela principal
janela = tk.Tk()

# Criação de um frame para organizar os elementos da interface
frame = Frame(janela, padx=40, pady=40)
frame.grid(column=1, row=1)

# Adiciona um rótulo com instruções para o usuário
Label(frame, text='Para saber seu IMC digite os valores abaixo.', pady=40).grid(column=1, row=1, columnspan=2)

# Rótulo e campo de entrada para o peso
Label(frame, text='Qual o seu peso (kg)?').grid(column=1, row=2)
peso = Entry(frame)
peso.grid(column=2, row=2)

# Rótulo e campo de entrada para a altura
Label(frame, text='Qual a sua altura (m)?').grid(column=1, row=3)
altura = Entry(frame)
altura.grid(column=2, row=3)

# Botão que calcula o IMC ao ser clicado
Button(frame, text='Calcular', command=calcula_imc).grid(column=2, row=4)

# Label que exibirá o resultado do cálculo do IMC
resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2)

# Define o título da janela principal
janela.title('Calculadora de IMC')

# Inicia o loop principal da interface gráfica
janela.mainloop()
