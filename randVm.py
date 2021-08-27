import random
import datetime
from pathlib import Path

def rand(vmax: int = 100, xmax: int = 50000) -> tuple:
    """
    Função retorna as variáveis aleatórias necessárias
    """
    # Velocidade aleatória
    vm = random.randint(-vmax, vmax)
    # Gerando uma lista de 2 tempos diferentes (função "sample"), escolhidos
    # de uma lista de inteiros entre 0:00 e 24:00, intervalos de 15 min
    t = sorted(random.sample([i/100 for i in range(0,2300,25)], 2))
    # Inicializando uma lista de posições
    x = list()
    # Primeira posição da lista gerada de forma aleatória
    x.append(random.randrange(-xmax, xmax,25)/100)
    # Segunda posição da lista criada de forma a fechar com t e vm
    x.append(vm*(t[1]-t[0]) + x[0])
    # return vm, th, tm, t, x
    return vm, t, x


def str_vars() -> list[str]:
    """
    Transformando tudo em strings para usar nos temaplates
    """
    # Chamando a função principal
    _, t, x = rand()
    x_string = [str(a).replace('.',',') for a in x]
    t_string = [str(datetime.timedelta(hours=a))[:-3] for a in t]
    deltax = [str(x[1]-x[0]).replace('.',',')]
    deltat = [str(datetime.timedelta(hours=t[1]-t[0]))[:-3]]
    # Objeto do movimento pode ser ônibus ou carro de passeio
    obj = [random.choice(['ônibus', 'carro de passeio', 'caminhão'])]
    # Objeto de retorno é uma concatenação de listas
    return obj + x_string + t_string + deltax + deltat

def exercicio() -> str:
    """
    Função geradora de exercícios aleatórios usando templates em ./templates
    """
    # Variáveis definidas no tamplate
    nomes = ['{obj}', '{x0}', '{x1}', '{t0}', '{t1}', '{deltax}', '{deltat}']
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
