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

x_string = [str(a).replace('.',',') for a in x]
t_string = [str(datetime.timedelta(hours=a))[:-3] for a in t]
deltax = str(x[1]-x[0]).replace('.',',')
deltat = str(datetime.timedelta(hours=t[1]-t[0]))[:-3]

ex = [x.read_text().\
      replace('{obj}',obj).\
      replace('{deltax}', deltax).\
      replace('{deltat}', deltat).\
      replace('{x0}', x_string[0]).\
      replace('{x1}', x_string[1]).\
      replace('{t1}', t_string[0]).\
      replace('{t0}', t_string[1]) \
      for x in Path(__file__).parent.joinpath("templates").iterdir()]

# Output uma escolha aleatória entre os exercícios
print(random.choice(ex))
