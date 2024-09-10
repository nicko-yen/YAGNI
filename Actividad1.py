class Calculadora:
    def sumar(self, Termino1, Termino2):
        return Termino1 + Termino2

    def restar(self, Termino1, Termino2):
        return Termino1 - Termino2


def ProbarSuma(Termino1, Termino2):
    calc = Calculadora()
    CalcularSuma = calc.sumar(Termino1, Termino2)
    print(f"{Termino1} + {Termino2} = {CalcularSuma}")


def ProbarResta(Termino1, Termino2):
    calc = Calculadora()
    CalcularResta = calc.restar(Termino1, Termino2)
    print(f"{Termino1} - {Termino2} = {CalcularResta}")


if __name__ == "__main__":
    variable1 = float(input("Ingrese el primer Termino: "))
    variable2 = float(input("Ingrese el segundo Termino: "))
    ProbarSuma(variable1, variable2)
    ProbarResta(variable1, variable2)