
import sqlite3
import tkinter as tk
from tkinter import messagebox


def conexao():
    return sqlite3.connect('banco_teste.db')

def criar_tabela():
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS dados(
                   
                   nome TEXT,
                   email TEXT,
                   idade TEXT,
                   endereço TEXT,
                   curso TEXT
                   
                   )''')
    conn.commit()
    conn.close()


def inserir():
    conn = conexao()
    cursor = conn.cursor()
    nome_ =nome.get()
    email_ = email.get() 

    if nome_ and email_: 
    
       cursor.execute('INSERT INTO dados VALUES(?,?)',(nome_, email_))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')
    else:
        messagebox.showerror('', 'DECLARE TODOS OS DADOS!')   




janela =  tk.Tk()


tk.Label(janela, text='nome: ').pack()

nome = tk.Entry(janela)
nome.pack()

tk.Label(janela, text='e-mail: ').pack()

email = tk.Entry(janela)
email.pack()


btn =  tk.Button(janela, text='inserir no banco', command=inserir)
btn.pack()



criar_tabela()

janela.mainloop()