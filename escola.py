from pessoa import Pessoa
from aluno import Aluno

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def cadastrarAluno(self,aluno: Aluno):
        self.alunos.append(aluno)

    def editarAluno(self, aluno:Aluno):
        for alu in self.alunos:
            if str(alu.matricula) == str(aluno.matricula):
                alu.nome = aluno.nome
                alu.idade = aluno.idade
                alu.curso = aluno.curso
                alu.nota = aluno.nota
                return True
        return False

    def removerAluno(self, matricula):
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula:
                self.alunos.remove(aluno)
                return True
        return False

    def listarAluno(self):
        return self.alunos


if __name__ == "__main__":
    escola = Escola("Menino Jesus")
    a1 = Aluno("Mateus", 3, "inf. III", 10)
    a2 = Aluno("Lucas", 2, "Inf. II", 8)
    escola.cadastrarAluno(a1)
    escola.cadastrarAluno(a2)
    print(escola.listarAluno())
    a1.nome = "Mateus Lima"
    escola.editarAluno(a1)
    print(escola.listarAluno())
    escola.removerAluno(a1.matricula)
    print(escola.listarAluno())
