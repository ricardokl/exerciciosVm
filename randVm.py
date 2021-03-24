import random
import datetime
from pathlib import Path

#função que retorna as variáveis necessárias
def rand():
    # Velocidade aleatória
    vm = random.randint(-100, 100)
    # Gerando uma lista de 2 tempos diferentes (função "sample"), escolhidos
    # de uma lista de inteiros entre 0:00 e 24:00, intervalos de 15 min
    t = sorted(random.sample([i/100 for i in range(0,2300,25)], 2))
    # Inicializando uma lista de posições
    x = list()
    # Primeira posição da lista gerada de forma aleatória
    x.append(random.randrange(-50000, 50000,25)/100)
    # Segunda posição da lista criada de forma a fechar com t e vm
    x.append(vm*(t[1]-t[0]) + x[0])
    # return vm, th, tm, t, x
    return vm, t, x


# Transformando tudo em strings
def str_vars():
    # Definindo as variáveis globalmente
    vm, t, x = rand()
    x_string = [str(a).replace('.',',') for a in x]
    t_string = [str(datetime.timedelta(hours=a))[:-3] for a in t]
    deltax = [str(x[1]-x[0]).replace('.',',')]
    deltat = [str(datetime.timedelta(hours=t[1]-t[0]))[:-3]]
    # Objeto do movimento pode ser ônibus ou carro de passeio
    obj = [random.choice(['ônibus', 'carro de passeio'])]
    return obj + x_string + t_string + deltax + deltat

# Função final
def exercicio():
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
    print(escolha)

# Chamando a função final
exercicio()
