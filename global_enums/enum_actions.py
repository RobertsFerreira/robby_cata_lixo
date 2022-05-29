from enum import Enum
from typing_extensions import Self


class Actions(Enum):
    MoveNorte = 0
    MoveSul = 1
    MoveLeste = 2
    MoveOeste = 3
    MoveAleatorio = 4
    FicaParado = 5
    PegaLata = 6

    def getAction(index: int) -> Self:
        if index == 0:
            return Actions.MoveNorte
        elif index == 1:
            return Actions.MoveSul
        elif index == 2:
            return Actions.MoveLeste
        elif index == 3:
            return Actions.MoveOeste
        elif index == 4:
            return Actions.MoveAleatorio
        elif index == 5:
            return Actions.FicaParado
        elif index == 6:
            return Actions.PegaLata
        else:
            Exception("Valor não identificado")

    def toString(self):
        if self == Actions.MoveNorte:
            return "Moveu para o Norte"
        elif self == Actions.MoveSul:
            return "Moveu para o Sul"
        elif self == Actions.MoveLeste:
            return "Moveu para o Leste"
        elif self == Actions.MoveOeste:
            return "Moveu para o Oeste"
        elif self == Actions.MoveAleatorio:
            return "Moveu Aleatoriamente"
        elif self == Actions.FicaParado:
            return "Ficou Parado"
        elif self == Actions.PegaLata:
            return "Acabou de pegar a Lata"
        else:
            Exception("Movimente Inválido")
