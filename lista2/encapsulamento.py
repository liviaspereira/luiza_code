"""Crie um professor de classe com atributos nome, idade e salário, onde
o salário deve ter um método privado que não pode ser acessado fora
da classe.
a. Crie um método para acessar o método privado, onde é passada
a identificação do usuário se ele pode ou não acessar."""


class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def _salario(self):
        if self.nome == "Jurandir":
            return "R$ 2450"


professor1 = Professor("Jurandir", "29")._salario()
professor2 = Professor("Marcos", "35")._salario()

print(professor1)
print(professor2)
