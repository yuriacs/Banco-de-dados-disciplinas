from __future__ import annotations
import jsonpickle
from json import loads

class Result:
    def toJSON(self):
        return loads(jsonpickle.encode(self, unpicklable=False))


class NotasResult(Result, object):
    def __init__(self, nota: NotasResult) -> None:
        self.nota = NotasResult(**nota)


class NomeResult(Result, object):
    def __init__(self, nome: NomeResult) -> None:
        self.nome = NomeResult(**nome)


class SucoFav_(Result, object):
    def __init__(self, sucofav: SucoFav_) -> None:
        self.sucofav = SucoFav_(**sucofav)


class Nota_:
    def __init__(
        self,
        num: float,
    ) -> None:
        self.num = num

        
class Nome_:
    def __init__(
        self,
        nome: str,
    ) -> None:
        self.nome = nome


class SucoFav_:
    def __init__(
        self,
        sucofav: str,
    ) -> None:
        self.sucofav = sucofav