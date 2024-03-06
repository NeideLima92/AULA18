from escola import Escola
from aluno import Aluno
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, nome: str):
        self.escola = Escola(nome)

        self.janela=Tk()
        self.janela.title(f"Sistema - {self.escola.nome}")

        self.label_matricula = Label (self.janela, text="Matrícula:", font="Calibri 14 bold", fg="Black")
        self.label_matricula.grid(row=0, column=0, sticky=W)
        self.txt_matricula = Entry(self.janela,  font="Calibri 14 bold", width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1, sticky=W)

        self.label_nome = Label(self.janela, text="Nome:", font="Calibri 14 bold", fg="Black")
        self.label_nome.grid(row=1, column=0, sticky=W)
        self.txt_nome = Entry(self.janela, font="Calibri 14 bold", width=27)
        self.txt_nome.grid(row=1, column=1, sticky=W)

        self.label_idade = Label(self.janela, text="Idade:", font="Calibri 14 bold", fg="Black")
        self.label_idade.grid(row=2, column=0, sticky=W)
        self.txt_idade = Entry(self.janela, font="Calibri 14 bold", width=27)
        self.txt_idade.grid(row=2, column=1, sticky=W)

        self.cursos= ["Infantil I","Infantil II","Infantil III","Infantil IV","Infantil V"]
        self.label_cursos = Label(self.janela, text="Curso:", font="Calibri 14 bold", fg="Black")
        self.label_cursos.grid(row=3, column=0, sticky=W)
        self.combo_cursos = ttk.Combobox (self.janela, values=self.cursos,width=40, state='readonly')
        self.combo_cursos.grid(row=3, column=1, sticky=W)

        self.label_nota = Label(self.janela, text="Nota:", font="Calibri 14 bold", fg="Black")
        self.label_nota.grid(row=4, column=0, sticky=W)
        self.txt_nota = Entry(self.janela, font="Calibri 14 bold", width=27)
        self.txt_nota.grid(row=4, column=1, sticky=W)

        self.button_Adicionar = Button(self.janela, text="Adicionar", font="Calibri 12 bold", fg="Black",
                              background="PaleGoldenrod", width=10,command=self.cadastrarAluno)
        self.button_Adicionar.grid(row=5, column=0)

        self.button_Editar = Button(self.janela, text="Editar", font="Calibri 12 bold", fg="Black",
                           background="PaleGoldenrod", width=10, command=self.editarAluno)
        self.button_Editar.grid(row=5, column=1)

        self.button_Excluir = Button(self.janela, text="Excluir", font="Calibri 12 bold", fg="Black",
                            background="PaleGoldenrod", width=10,command=self.deletarAluno)
        self.button_Excluir.grid(row=5, column=2)

        #self.frame = Frame(self.janela)
        #self.frame.grid(row=6, columnspan=3)

        self.colunas = ["Matricula", "Nome", "Idade", "Curso", "nota"]
        self.tabela = ttk.Treeview(self.janela, columns=self.colunas, show="headings")
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)

        self.tabela.bind("<ButtonRelease-1>",self.selecionarAluno)
        self.tabela.grid(row=6, columnspan=3)

        self.atualizarTabela()
        self.janela.mainloop()

    def cadastrarAluno(self):
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)

        self.escola.alunos.append(aluno)
        messagebox.showinfo("Sucesso!","Aluno cadastrado com sucesso!")
        print(self.escola.alunos)
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0,END)
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.combo_cursos.set("")
        self.txt_nota.delete(0, END)

    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        for aluno in self.escola.alunos:
            self.tabela.insert("",END,values= (aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))

    def selecionarAluno(self,event):
        linhaselecionada = self.tabela.selection()[0]
        valores = self.tabela.item(linhaselecionada)['values']
        self.limparCampos()

        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0,valores[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0,valores[1])
        self.txt_idade.insert(0,valores[2])
        self.combo_cursos.set(valores[3])
        self.txt_nota.insert(0,valores[4])

    def deletarAluno(self):
        matricula = self.txt_matricula.get()
        opcao = messagebox.askyesno("Confirmação de alteração!", "Deseja remover os dados!")
        if opcao:
            self.escola.removerAluno(matricula)
            messagebox.showinfo("Sucesso!","Aluno removido com sucesso!")
        print(self.escola.alunos)
        self.limparCampos()
        self.atualizarTabela()

    def editarAluno(self):
        matricula = self.txt_matricula.get()
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        aluno.matricula= matricula
        opcao = messagebox.askyesno("Tem certeza?", "Deseja alterar os dados?")
        if opcao:
            self.escola.editarAluno(aluno)
            messagebox.showinfo("Sucesso!", "Dados alterados com sucesso!")
        print(self.escola.alunos)
        self.limparCampos()
        self.atualizarTabela()




App("CEI Menino Jesus")
