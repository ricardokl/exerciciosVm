import random
import datetime
from pathlib import Path

# Gerando um valor inteiro aleatório para a velocidade média
vm = random.randint(-100, 100)

# Gerando uma lista de 2 tempos diferentes (função "sample"), escolhidos
# de uma lista de inteiros entre 0 e 24
th = sorted(random.sample(range(0,23), 2))
tm = random.sample([00,15,30,45]*2,2)
t = [th[x] + tm[x]/60 for x in range(len(th))]

# Inicializando uma lista de posições
x = list()
# Primeira posição da lista gerada de forma aleatória
x.append(random.randint(-500, 500))
# Segunda posição da lista criada de forma a fechar com t e vm
x.append(vm*(t[1]-t[0]) + x[0])

# Objeto do movimento pode ser ônibus ou carro de passeio
obj = random.choice(['ônibus', 'carro de passeio'])

# Transformando tudo em strings
x_string = [str(a).replace('.',',') for a in x]
t_string = [str(datetime.timedelta(hours=a))[:-3] for a in t]
deltax = str(x[1]-x[0]).replace('.',',')
deltat = str(datetime.timedelta(hours=t[1]-t[0]))[:-3]

# Dicionário de substituições
subs = {'{obj}':obj, \
        '{deltax}': deltax, \
        '{deltat}': deltat, \
        '{x0}': x_string[0], \
        '{x1}': x_string[1], \
        '{t1}': t_string[0], \
        '{t0}': t_string[1]}

# Lista com todos os caminhos dos arquivos da pasta /template
templates = [x for x in Path(__file__).parent.joinpath("templates").iterdir()]

# Escolhendo um arquivo aleatório e lendo o texto dele
escolha = random.choice(templates).read_text()

# Loop substituindo todos as variáveis no texto
for pair in subs.items():
    escolha = escolha.replace(pair[0],pair[1])

# Print do resultado final
print(escolha)
