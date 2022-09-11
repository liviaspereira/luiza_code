"""Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
3. Escreva uma classe “PessoaJurica” e herde Pessoa, agora
modificando o comportamento, retorne o cnpj. Crie uma instância e
acesse os dados"""

from classe import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(cpf, nome, idade)

    def input_sobrenome_cidade(self, sobrenome, cidade):
        self.sobrenome = sobrenome
        self.cidade = cidade


class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome, idade):
        super().__init__(cnpj, nome, idade)

    def input_cidade(self, categoria):
        self.categoria = categoria

    def __repr__(self) -> str:
        return f"{self.nome} de CNPJ {self.cpf} possui {self.idade} anos de idade"


pessoa1 = PessoaFisica("22222222222", "Astrogilda", "96")
pessoa1.input_sobrenome_cidade("da Silva", "São Paulo")

pessoajuridica = PessoaJuridica("12345678901234", "Empresa X", "104")
pessoajuridica.input_cidade("Comércio")


print(pessoa1)
print(pessoajuridica)
