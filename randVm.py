from random import randint, choice
from datetime import timedelta

Transporte_escolhido = choice(["carro", "a pé", "ônibus", "bicicleta", "motocicleta", "skate"])

def info(vmin, vmax, dtmin, dtmax):
    Vm = randint(vmin, vmax)
    ti = (randint(40, 64))*15
    dt = (randint(dtmin, dtmax))*15
    diffinsec = dt*60
    d = (Vm*diffinsec)/1000
    start = str(timedelta(minutes=ti))
    end = str(timedelta(minutes=ti + dt))
    return Vm, d, start, end

if Transporte_escolhido == "carro":
    Vm, d, start, end = info(12, 23, 1, 24)
    print(f"Uma pessoa que saiu de casa com seu {Transporte_escolhido} às {start[0:5]} horas chegou ao seu destino às {end[0:5]}."
          f" Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
if Transporte_escolhido == "a pé":
    Vm, d, start, end = info(1, 2, 1, 10)
    print(f"Uma pessoa que saiu de casa {Transporte_escolhido} às {start[0:5]} horas chegou ao seu destino às {end[0:5]}."
          f" Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
if Transporte_escolhido == "ônibus":
    Vm, d, start, end = info(12, 23, 1, 28)
    print(f"Uma pessoa que acabou de sair de uma estação de {Transporte_escolhido} às {start[0:5]} horas chegou ao seu destino às {end[0:5]}."
          f" Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
if Transporte_escolhido == "bicicleta":
    Vm, d, start, end = info(2, 6, 1, 12)
    print(f"Uma pessoa que saiu de casa com sua {Transporte_escolhido} às {start[0:5]} horas chegou ao seu destino às {end[0:5]}."
          f" Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
if Transporte_escolhido == "motocicleta":
    Vm, d, start, end = info(11, 30, 1, 20)
    print(f"Uma pessoa que saiu de casa com sua {Transporte_escolhido} às {start[0:5]} horas chegou ao seu destino às {end[0:5]}."
          f" Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
if Transporte_escolhido == "skate":
    Vm, d, start, end = info(1, 4, 1, 8)
    print(f"Uma pessoa que saiu de casa com seu {Transporte_escolhido} às {start[0:5]} horas chegou ao seu destino às {end[0:5]}."
          f" Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")

R = input(print("Qual é a sua resposta? "))
Vm = str(Vm)
Vm = Vm + "m/s"
if Vm == R:
    print("Boa! Você acertou!!!")
else:
    print(f"A resposta correta era {Vm}. Tente novamente!")
