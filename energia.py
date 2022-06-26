import random
from pathlib import Path
from numpy import array


# Como fazer com vários corpos? Talvez as váriáveis devem ser definidas como
# listas?
# colocar variáveis randomizadas

class ExEnergia:
    def __init__(self, m: list[int],v: list[int],y: list[int], g:int = 10) -> None:
        """
        Exercicio de energia, envolvendo cinética, potencial, etc
        Massa, velocidade e h são listas de inteiros, com valores inicial e final
        """
        # TODO: Modificar o diretório de templates
        templates = [x for x in
            Path(__file__).parent.joinpath("templates").joinpath("energia").iterdir()]
        self.texto: str = random.choice(templates).read_text()
        self.v = array(v)
        self.m = array(m)
        self.y = array(y)
        self.Ec = (self.m)/2 * self.v**2
        self.Epg = self.m * g * self.y
        self.Et = self.Ec + self.Epg

    def rand(self, m: int = 10,v: int = 50,y: int = 100, g:int = 10) -> None:
        self.v = array(v)
        self.m = array(m)
        self.y = array(y)
        self.Ec = (1/2) * self.m * self.v**2
        self.Epg = self.m * g * self.y
        self.Et = self.Ec + self.Epg
