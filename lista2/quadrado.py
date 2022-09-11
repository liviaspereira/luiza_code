"""Escreva uma classe “Quadrado”, crie dois métodos que retornem a
área do quadrado e o perímetro, não crie a instância nesse exercício."""


class Quadrado:
    @staticmethod
    def area(lado):
        return lado * 2

    @staticmethod
    def perimetro(lado):
        return lado * 4


if __name__ == "__main__":
    area = Quadrado.area(5)
    print(f"O perimetro é de: {area}")

    perimetro = Quadrado.perimetro(5)
    print(f"O perimentro é de: {perimetro}")
