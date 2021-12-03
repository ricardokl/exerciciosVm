import random
import datetime
from pathlib import Path

multi = 4

def mru(vmax: int = 100, xmax: int = 500, dtmax: int = 6) -> tuple:
    """
    Função retorna as variáveis aleatórias necessárias
    """
    # Velocidade aleatória
    v = random.randint(-vmax, vmax)
    # Gerando o intervalo de tempo do movimento
    dt = random.randint(1,dtmax*4)/4
    # Inicializando as listas de tempo e posição
    t, x = list(), list()
    # Primeiro valor do tempo gerado randomicamente
    t.append(random.randint(0,18*4)/4)
    # Segundo valor do tempo dado pelo primeiro mais o intervalo
    t.append(t[0]+dt)
    # Posição inicial aleatória
    x.append(random.randint(-xmax*4, xmax*4)/4)
    # Posição final dada pela equação
    x.append(v*dt + x[0])
    dx = x[1]-x[0]
    return v, t, x, dt, dx

def str_vars() -> list[str]:
    """
    Transformando tudo em strings para usar nos temaplates
    """
    # Chamando a função principal
    v, t, x, dt, dx = mru()
    # Transformando v em string
    v_string = [str(v)]
    # Transformando x em strings e trocando pontos por virgulas
    x_string = [str(a).replace('.',',') for a in x]
    # [:-3] retira os segundos da string
    t_string = [str(datetime.timedelta(hours=a))[:-3] for a in t]
    # Transformando os deltas em strings
    dx_string = [str(dx).replace('.',',')]
    dt_string = [str(datetime.timedelta(hours=dt))[:-3]]
    # Objeto do movimento pode ser ônibus ou carro de passeio
    obj = [random.choice(['ônibus', 'carro de passeio', 'caminhão'])]
    # Objeto de retorno é uma concatenação de listas
    return obj + v_string + t_string + x_string + dx_string + dt_string

def exercicio() -> str:
    """
    Função geradora de exercícios aleatórios usando templates em ./templates
    """
    # Variáveis definidas no tamplate
    nomes = ['{obj}', '{v}', '{t0}', '{t1}', '{x0}', '{x1}', '{deltax}', '{deltat}']
    # Dicionário com as substituições
    subs = {nome:var for nome, var in zip(nomes,str_vars())}
    # Lista com todos os caminhos dos arquivos da pasta /template
    templates = [x for x in Path(__file__).parent.joinpath("templates").iterdir()]
    # Escolhendo um arquivo aleatório e lendo o texto dele
    escolha = random.choice(templates).read_text()
    # Loop substituindo todos as variáveis no texto
    for i in subs.items():
        escolha = escolha.replace(i[0],i[1])
    return escolha

if __name__ ==  '__main__':
    print(exercicio())
