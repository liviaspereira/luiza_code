"""Exemplo Polimorfismo e Ducktyping"""

from typing import List


class Planta:
    def __init__(self, numero_petalas=10):
        self.petalas = numero_petalas

    def tipo(self):
        return "Briofita"

    def eh_bipede(self):
        return False


class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def eh_bipede(self):
        return self.numero_patas == 2


class Gato(Animal):
    def __init__(self, numero_patas=4):
        self.numero_patas = numero_patas


class Macaco(Animal):
    def __init__(self, numero_patas=2):
        self.numero_patas = numero_patas


def checa_aniamais(lista_animais: List[Animal]):
    for animal in lista_animais:
        if animal.eh_bipede():
            print(animal, "é bipede")
        else:
            print(animal, "não é bipede")


lista = [Gato(), Macaco(), Gato(), Planta()]
checa_aniamais(lista)
