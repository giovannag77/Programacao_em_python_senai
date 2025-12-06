import tkinter as tk

def nomes ():
    nome = input_1.get()
    print(nome)

    idade = input_2.get()
    print(idade)

    email = input_3.get()
    print(email)

    endereço = input_4.get()
    print(endereço)

    celular = input_5.get()
    print(celular)

    cep = input_6.get()
    print(cep)

    cidade = input_7.get()
    print(cidade)

    cursos = input_8.get()
    print(cursos)

janela = tk.Tk()
janela.geometry('1700x750')
janela.config(bg = '#454545')

tk.Label(janela, text = 'CADASTRO DE CLIENTES',bg = '#DCD7D7', fg = 'BLACK' , font=('Montserrat', 20) ).grid(row=1, column=1, pady=15)


fr1 =  tk.Frame(janela, bg = '#DCD7D7')
fr1.grid(columnspan=3)



nome = tk.Label(fr1, text = 'NOME', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
nome.grid(row = 1, column = 2, pady=12, padx=12)

idade = tk.Label(fr1, text = 'IDADE', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
idade.grid(row = 1, column = 3, pady=12, padx=12)

email = tk.Label(fr1, text = 'EMAIL', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
email.grid(row = 1, column = 4, pady=12, padx=12)

endereço = tk.Label(fr1, text = 'ENDEREÇO', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
endereço.grid(row = 1, column = 5,pady=12, padx=12)

celular = tk.Label(fr1, text = 'CELULAR', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
celular.grid(row = 1, column = 6, pady=12, padx=12)

cep = tk.Label(fr1, text = 'CEP',bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
cep.grid(row = 1, column = 7, pady=12, padx=12)

cidade = tk.Label(fr1, text = 'CIDADE', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
cidade.grid(row = 1, column = 8, pady=12, padx=12)

cursos = tk.Label(fr1, text = 'CURSOS', bg = '#DCD7D7', fg = 'BLACK', font=('Montserrat', 15))
cursos.grid(row = 1, column = 9, pady=12, padx=12)



input_1 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_1.grid(row=2, column=2, pady=1, padx=1)

input_2 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_2.grid(row=2, column=3, pady=12, padx=12)

input_3 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_3.grid(row=2, column=4, pady=12, padx=12)

input_4 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_4.grid(row=2, column=5, pady=12, padx=12)

input_5 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_5.grid(row=2, column=6, pady=12, padx=12)

input_6 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_6.grid(row=2, column=7, pady=12, padx=12)

input_7 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_7.grid(row=2, column=8, pady=12, padx=12)

input_8 =  tk.Entry(fr1,font=('Montserrat', 12), width=12)
input_8.grid(row=2, column=9, pady=12, padx=12)




fr2 = tk.Frame(janela, bg = '#454545')
fr2.grid(columnspan=3 )



btn_click =  tk.Button(fr2, text='CLIQUE', font=('Montserrat', 12), bg = 'white', width=12, command = nomes)
btn_click.grid(row=4, column=1, pady=20)

janela.mainloop()