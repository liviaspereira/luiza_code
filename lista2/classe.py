""" Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno do documento, o retorno do nome e
verificação de tipo de pessoa, onde um método irá receber como parâmetro “F” ou “N” para trazer fumante ou não fumante."""


class Pessoa:
    def __init__(self, cpf, nome, idade, fumante="N"):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.fumante = fumante

    def __repr__(self) -> str:
        return f"{self.nome} de CPF {self.cpf} possui {self.idade} anos de idade"

    def eh_fumante(self):
        if self.fumante == "F":
            return f"{self.nome} de CPF {self.cpf} possui {self.idade} anos de idade e é fumante"

        if self.fumante == "N":
            return f"{self.nome} de CPF {self.cpf} possui {self.idade} anos de idade e não é fumante"


if __name__ == "__main__":
    pessoa1 = Pessoa("66666666666", "Astrogilda", "96", "F")
    pessoa2 = Pessoa("44444444444", "Jurumaina", "12", "F")
    pessoa3 = Pessoa("99999999999", "Zilmar", "86", "N")

    print(pessoa1.eh_fumante())
    print(pessoa2.eh_fumante())
    print(pessoa3.eh_fumante())
