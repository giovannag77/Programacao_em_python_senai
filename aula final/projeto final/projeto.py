import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#  BANCO 
def conectar():
    return sqlite3.connect('saude.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    peso REAL NOT NULL,
    altura REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

#IMC 
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"{imc:.1f} - Abaixo do peso"
    elif imc < 25:
        return f"{imc:.1f} - Normal"
    elif imc < 30:
        return f"{imc:.1f} - Sobrepeso"
    else:
        return f"{imc:.1f} - Obesidade"

#  CRUD 
def inserir_dados():

    nome = entry_nome.get()
    idade = int(entry_idade.get())
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    if nome and idade and peso and altura:
        conn = conectar()
        c = conn.cursor()
        c.execute("INSERT INTO usuarios (nome, idade, peso, altura) VALUES (?, ?, ?, ?)",(nome, idade, peso, altura))
        conn.commit()
        conn.close()
        limpar_campos()
        mostrar_usuario()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente")

def mostrar_usuario():
    # Limpa a tabela
    for item in tree.get_children():
        tree.delete(item)

    # Conecta ao banco
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()  # AQUI o erro era esse
    conn.close()

    # Insere os dados na Treeview
    for usuario in usuarios:
        if len(usuario) < 5:  
         resultado = calcular_imc(usuario[2], usuario[3])
         tree.insert("", "end", values=(*usuario, resultado))




def atualizar():
    selecionado = tree.selection()
    try:
        
        id_user = tree.item(selecionado)['values'][0]

        nome = entry_nome.get()
        idade = int(entry_idade.get())
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        conn = conectar()
        c = conn.cursor()
        c.execute("""
        UPDATE usuarios
        SET nome=?, idade=?, peso=?, altura=? WHERE nome =? 
        """, (nome, idade, peso, altura, id_user))

        conn.commit()
        conn.close()
        mostrar_usuario()
        messagebox.showinfo("Sucesso", "Dados atualizados!")
    except:
        messagebox.showerror("Erro", "Selecione um registro")

def deletar():
    selecionado = tree.selection()
    if selecionado:
        
        id_user = tree.item(selecionado)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute("DELETE FROM usuarios WHERE nome=?", (id_user,))
        conn.commit()
        conn.close()
        mostrar_usuario()
        messagebox.showinfo("Sucesso", "Registro deletado!")
    else:
        messagebox.showerror("Erro", "Selecione um registro")

def consultar():
    nome = entry_nome.get()
    for item in tree.get_children():
        tree.delete(item)
        conn = conectar()
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE nome LIKE ?", ('%' + nome + '%',))
        
        dados = c.fetchall()
        for n in dados:
              imc = round(n[2]/(n[3]**2),2)
              print (imc)
              if imc <=18:
                  messagebox.showinfo('','ABAIXO DO PESO -> {} '.format(imc))
              elif imc <=25:
                 messagebox.showinfo('','NORMAL -> {} '.format(imc))
              elif imc <=30:
                 messagebox.showinfo('','ACIMA DO PESO -> {} '.format(imc))
              else:
                 messagebox.showinfo('','OBESIDADE -> {} '.format(imc))
    
      
    #     messagebox.showinfo('imc',imc)
    # for usuario in dados:
    #     resultado = calcular_imc(usuario[3], usuario[4])
    #     tree.insert("", "end", values=(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], resultado))
    #     conn.close()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)

#  INTERFACE 
root = customtkinter.CTk()
root.title("Calculadora IMC")
root.geometry("750x500")
icone = 'img.ico'
root.iconbitmap(icone)

frame = customtkinter.CTkFrame(root)
frame.pack(pady=10)

entry_nome = customtkinter.CTkEntry(frame, placeholder_text="Nome")
entry_nome.grid(row=0, column=0, padx=5)

entry_idade = customtkinter.CTkEntry(frame, placeholder_text="Idade")
entry_idade.grid(row=0, column=1, padx=5)

entry_peso = customtkinter.CTkEntry(frame, placeholder_text="Peso (kg)")
entry_peso.grid(row=0, column=2, padx=5)

entry_altura = customtkinter.CTkEntry(frame, placeholder_text="Altura (m)")
entry_altura.grid(row=0, column=3, padx=5)

btn_frame = customtkinter.CTkFrame(root)
btn_frame.pack(pady=10)

customtkinter.CTkButton(btn_frame, text="Salvar", command=inserir_dados).grid(row=0, column=0, padx=5)

customtkinter.CTkButton(btn_frame, text="Atualizar", command=atualizar).grid(row=0, column=1, padx=5)

customtkinter.CTkButton(btn_frame, text="Deletar", command=deletar).grid(row=0, column=2, padx=5)

customtkinter.CTkButton(btn_frame, text="Consultar", command=consultar).grid(row=0, column=3, padx=5)

columns = ("NOME","IDADE", "PESO", "ALTURA", "RESULTADO")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(expand=True, fill="both")

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()
root.mainloop()