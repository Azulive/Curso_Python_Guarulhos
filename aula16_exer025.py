# Crie um formulário em Tkinter, contendo, nome, idade, e-mail, endereço, celular.

# Problema: Sistema de Cadastro de Clientes

# Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes. 
# O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço e celular.

# Atividade:
# Crie um formulário em Tkinter que contenha os seguintes campos:
# Nome
# Idade
# E-mail
# Endereço
# Celular
# O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.


import tkinter as tk


def cadastro():
    nome_texto = nome_input.get() 
    idade_texto = idade_input.get() 
    email_texto = email_input.get()
    endereco_texto = endereco_input.get()
    celular_texto = celular_input.get()
    nome_resultado.config(text=nome_texto) 
    idade_resultado.config(text=idade_texto)
    email_resultado.config(text=email_texto)
    endereco_resultado.config(text=endereco_texto)
    celular_resultado.config(text=celular_texto)
    

janela = tk.Tk()
janela.title('Cadastro de usúario')
janela.geometry('350x300')


nome_input = tk.Entry(janela)
nome_input.grid(column=2, row=2)
nome = tk.Label(janela, text='Nome')
nome.grid(column=1, row=2)

idade_input = tk.Entry(janela)
idade_input.grid(column=2, row=3)
idade = tk.Label(janela, text='Idade')
idade.grid(column=1, row=3)

email_input = tk.Entry(janela)
email_input.grid(column=2, row=4)
email = tk.Label(janela,text='E-mail')
email.grid(column=1, row=4)

endereco_input = tk.Entry(janela)
endereco_input.grid(column=2, row=5)
endereco = tk.Label(janela, text='Endereço')
endereco.grid(column=1, row=5)

celular_input = tk.Entry(janela)
celular_input.grid(column=2, row=6)
celular = tk.Label(janela, text='Celular')
celular.grid(column=1, row=6)

btn_enviar = tk.Button(janela, text='Enviar', width=15, command=cadastro)
btn_enviar.grid(column=4, row=4)

nome_resultado = tk.Label(janela, text='') 
nome_resultado.grid(column=2, row=8) 
idade_resultado = tk.Label(janela, text='') 
idade_resultado.grid(column=2, row=9)
email_resultado = tk.Label(janela, text='')
email_resultado.grid(column=2, row=10)
endereco_resultado = tk.Label(janela, text='')
endereco_resultado.grid(column=2, row=11)
celular_resultado = tk.Label(janela, text='')
celular_resultado.grid(column=2, row=12)

janela.mainloop()