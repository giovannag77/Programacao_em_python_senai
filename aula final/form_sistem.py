import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk


def conectar():
    return sqlite3.connect('teste.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
              
                  id INTEGER NOT NULL,
                  nome TEXT NOT NULL,
                  email TEXT NOT NULL
              
          )
       ''')
    conn.commit()
    conn.close()

criar_tabela()

# CRUD 
# CREATE -  criando os dados
def inserir_usuario():
    nome  = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()

    if nome and cpf and email:
        conn =  conectar()
        c =  conn.cursor()
        c.execute('INSERT INTO usuarios(id,nome,email) VALUES(?,?,?)', (cpf, nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'DADOS NÃO INSERIDOS')    

# read -  lendo 

def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn =  conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", 'end', values=(usuario[0], usuario[1],usuario[2]))       
    conn.close()



# update     -  atualizando 


def atualizar():
    selecao =  tree.selection()
    if selecao:
        user_id =  tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()
        novo_email = entry_email.get()
        novo_cpf = entry_cpf.get()

        if novo_email and novo_nome:
            conn =  conectar()
            c =  conn.cursor()
            c.execute('UPDATE usuarios  SET nome = ?, email = ?   WHERE id = ?', (novo_nome, novo_email, user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()
        else:
            messagebox.showerror('ERRO', 'OCORREU UM ERRO!')
    else:
        messagebox.showwarning('', 'OCORREU UM ERRO DESCONHECIDO')            

# DELETE  -  DELETAR O DADO 

def deletar():

    selecao =  tree.selection()
    if selecao:
        user_id =  tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADOS DELETADOS')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'OCORREU UM ERRO')    
        







# interface grafica


root =  tk.Tk()
root.title('CRUD')
root.configure( bg = 'orange')
icone = 'img.ico'
root.iconbitmap(icone)


fr1 = tk.Frame(root, bg='orange')
fr1.grid(columnspan=3)



label_nome = tk.Label(fr1, text='Nome: ', font=('arial', 12))
label_nome.grid(row=0, column=0, pady = 5)

entry_nome = tk.Entry(fr1, font=('arial', 12))
entry_nome.grid(row=0, column=1, pady = 5)

label_cpf = tk.Label(fr1, text='cpf: ', font=('arial', 12))
label_cpf.grid(row=1, column=0, pady = 5)

entry_cpf = tk.Entry(fr1, font=('arial', 12))
entry_cpf.grid(row=1, column=1, pady = 5)

label_email = tk.Label(fr1, text='e - mail: ', font=('arial', 12))
label_email.grid(row=2, column=0, pady = 5)

entry_email = tk.Entry(fr1, font=('arial', 12))
entry_email.grid(row=2, column=1, pady = 5)

fr2 = tk.Frame(root, bg = 'orange')
fr2.grid(columnspan=3, pady=20)

btn_salvar = tk.Button(fr2, text='salvar', font=('arial', 12),command=inserir_usuario)
btn_salvar.grid(row=4, column=0, pady = 5, padx=5)

btn_atualizar = tk.Button(fr2, text='atualizar', font=('arial', 12), command=atualizar)
btn_atualizar.grid(row=4, column=1, pady = 5, padx=5)

btn_deletar = tk.Button(fr2, text='deletar', font=('arial', 12), command=deletar)
btn_deletar.grid(row=4, column=2, pady = 5, padx=5)


columns = ('CPF', 'NOME', 'E-MAIL')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.grid(row=6,column=0)


for col in columns:
    tree.heading(col, text=col)


criar_tabela()
mostrar_usuario()



root.mainloop()



