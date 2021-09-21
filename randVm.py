import random
import datetime
Transportes = ["carro", "a pé", "ônibus", "bicicleta", "motocicleta", "skate"]
Transporte_escolhido = random.choice(Transportes)
if Transporte_escolhido == "carro":
    Vm = random.randint(12, 23)
    ti = (random.randint(40, 64))*15
    td = random.randint(0, 24)*15
    diffinsec = (td*60)
    d = (Vm*diffinsec)/1000
    now = datetime.timedelta(minutes=ti)
    tdiff = datetime.timedelta(minutes=td)
    then = str(datetime.timedelta(minutes=ti + td))
    now = str(now)
    tdiff = str(tdiff)
    print(f"Uma pessoa que saiu de casa com seu {Transporte_escolhido} às {now[0:5]} horas chegou ao seu destino às {then[0:5]}. Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print(f"A resposta correta era {Vm}. Tente novamente!")

if Transporte_escolhido == "a pé":
    Vm = random.randint(1, 2)
    ti = (random.randint(40, 64))*15
    td = random.randint(0, 10)*15
    diffinsec = (td*60)
    d = (Vm*diffinsec)/1000
    now = datetime.timedelta(minutes=ti)
    tdiff = datetime.timedelta(minutes=td)
    then = str(datetime.timedelta(minutes=ti + td))
    now = str(now)
    tdiff = str(tdiff)
    print(f"Uma pessoa que saiu de casa {Transporte_escolhido} às {now[0:5]} horas chegou ao seu destino às {then[0:5]}. Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print(f"A resposta correta era {Vm}. Tente novamente!")
if Transporte_escolhido == "ônibus":
    Vm = random.randint(12, 23)
    ti = (random.randint(40, 64))*15
    td = random.randint(0, 28)*15
    diffinsec = (td*60)
    d = (Vm*diffinsec)/1000
    now = datetime.timedelta(minutes=ti)
    tdiff = datetime.timedelta(minutes=td)
    then = str(datetime.timedelta(minutes=ti + td))
    now = str(now)
    tdiff = str(tdiff)
    print(f"Uma pessoa que acabou de sair de uma estação de {Transporte_escolhido} às {now[0:5]} horas chegou ao seu destino às {then[0:5]}. Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print(f"A resposta correta era {Vm}. Tente novamente!")
if Transporte_escolhido == "bicicleta":
    Vm = random.randint(2, 6)
    ti = (random.randint(40, 64))*15
    td = random.randint(0, 12)*15
    diffinsec = (td*60)
    d = (Vm*diffinsec)/1000
    now = datetime.timedelta(minutes=ti)
    tdiff = datetime.timedelta(minutes=td)
    then = str(datetime.timedelta(minutes=ti + td))
    now = str(now)
    tdiff = str(tdiff)
    print(f"Uma pessoa que saiu de casa com sua {Transporte_escolhido} às {now[0:5]} horas chegou ao seu destino às {then[0:5]}. Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print(f"A resposta correta era {Vm}. Tente novamente!")
if Transporte_escolhido == "motocicleta":
    Vm = random.randint(11, 30)
    ti = (random.randint(40, 64))*15
    td = random.randint(0, 20)*15
    diffinsec = (td*60)
    d = (Vm*diffinsec)/1000
    now = datetime.timedelta(minutes=ti)
    tdiff = datetime.timedelta(minutes=td)
    then = str(datetime.timedelta(minutes=ti + td))
    now = str(now)
    tdiff = str(tdiff)
    print(f"Uma pessoa que saiu de casa com sua {Transporte_escolhido} às {now[0:5]} horas chegou ao seu destino às {then[0:5]}. Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print(f"A resposta correta era {Vm}. Tente novamente!")
if Transporte_escolhido == "skate":
    Vm = random.randint(1, 4)
    ti = (random.randint(40, 64))*15
    td = random.randint(0, 8)*15
    diffinsec = (td*60)
    d = (Vm*diffinsec)/1000
    now = datetime.timedelta(minutes=ti)
    tdiff = datetime.timedelta(minutes=td)
    then = str(datetime.timedelta(minutes=ti + td))
    now = str(now)
    tdiff = str(tdiff)
    print(f"Uma pessoa que saiu de casa com seu {Transporte_escolhido} às {now[0:5]} horas chegou ao seu destino às {then[0:5]}. Sabendo que a distância percorrida por essa pessoa foi de {d}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?")
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print(f"A resposta correta era {Vm}. Tente novamente!")
