import random
import datetime
from pathlib import Path
from dataclasses import dataclass, field

# path = Path(__file__)

@dataclass(slots=True)
class mru:
    def __init__(self, vmax: int = 100, xmax: int = 500, dtmax: int = 6) -> None:
        """
        Inicialisa um exercício, gerando um texto e os valores a serem
        substituidos
        """
        templates = [x for x in Path(__file__).parent.joinpath("templates").iterdir()]
        self.texto = random.choice(templates).read_text()
        # Velocidade aleatória
        self.v = random.randint(-vmax, vmax)
        # Gerando o intervalo de tempo do movimento
        self.dt = random.randint(1,dtmax*4)/4
        # Inicializando as listas de tempo e posição
        self.t, self.x = list(), list()
        # Primeiro valor do tempo gerado randomicamente
        self.t.append(random.randint(0,18*4)/4)
        # Segundo valor do tempo dado pelo primeiro mais o intervalo
        self.t.append(self.t[0]+self.dt)
        # Posição inicial aleatória
        self.x.append(random.randint(-xmax*4, xmax*4)/4)
        # Posição final dada pela equação
        self.x.append(self.v*self.dt + self.x[0])
        self.dx = self.x[1]-self.x[0]

    def rand(self, vmax: int = 100, xmax: int = 500, dtmax: int = 6) -> None:
        """
        Gera novas variáveis randomizadas
        """
        self.v = random.randint(-vmax, vmax)
        # Gerando o intervalo de tempo do movimento
        self.dt = random.randint(1,dtmax*4)/4
        # Inicializando as listas de tempo e posição
        self.t, self.x = list(), list()
        # Primeiro valor do tempo gerado randomicamente
        self.t.append(random.randint(0,18*4)/4)
        # Segundo valor do tempo dado pelo primeiro mais o intervalo
        self.t.append(self.t[0]+self.dt)
        # Posição inicial aleatória
        self.x.append(random.randint(-xmax*4, xmax*4)/4)
        # Posição final dada pela equação
        self.x.append(self.v*self.dt + self.x[0])
        self.dx = self.x[1]-self.x[0]

    def subs(self) -> str:
        """
        Transforma as variáveis em strings e substitui no texto gerado
        """
        # Transformando v em string
        v_string = [str(self.v)]
        # Transformando x em strings e trocando pontos por virgulas
        x_string = [str(a).replace('.',',') for a in self.x]
        # [:-3] retira os segundos da string
        t_string = [str(datetime.timedelta(hours=a))[:-3] for a in self.t]
        # Transformando os deltas em strings
        dx_string = [str(self.dx).replace('.',',')]
        dt_string = [str(datetime.timedelta(hours=self.dt))[:-3]]
        # Objeto do movimento pode ser ônibus ou carro de passeio
        obj = [random.choice(['ônibus', 'carro de passeio', 'caminhão'])]
        # Variáveis definidas no tamplate
        nomes = ['{obj}', '{v}', '{t0}', '{t1}', '{x0}', '{x1}', '{deltax}', '{deltat}']
        valores = obj + v_string + t_string + x_string + dx_string + dt_string
        # Dicionário com as substituições
        subs = {nome:var for nome, var in zip(nomes,valores)}
        # Lista com todos os caminhos dos arquivos da pasta /template
        # Loop substituindo todos as variáveis no texto
        texto_final = self.texto
        for i in subs.items():
            texto_final = texto_final.replace(i[0],i[1])
        return texto_final
