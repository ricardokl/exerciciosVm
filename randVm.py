import random
import datetime
Transportes = ["andando", "carro", "ônibus", "bicicleta", "motocicleta", "skate"]
Transporte_escolhido = random.choice(Transportes)
if Transporte_escolhido == "carro":
    Vm = random.randint(12, 28)
    mi = random.randint(0, 59)
    md = random.randint(0, 59)
    hi = random.randint(8, 16)
    hd = random.randint(0, 6)
    if hd == 0:
        md = random.randint(1, 59)
    diffinsec = ((hd*3600)+(md*60))
    d = (Vm*diffinsec)/1000
    now = datetime.datetime(2000, 1, 1, hi, mi)
    tdiff = datetime.timedelta(hours=hd, minutes=md)
    then = str(now + tdiff)
    now = str(now)
    tdiff = str(tdiff)
    print("Uma pessoa que saiu de casa com seu {} às {} horas chegou ao seu destino às {}. Sabendo que a distância percorrida por essa pessoa foi de {}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?".format(Transporte_escolhido, now[11:16], then[11:16], d))
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print("A resposta correta era {}. Tente novamente!".format(Vm))

if Transporte_escolhido == "andando":
    Vm = random.randint(1, 3)
    mi = random.randint(0, 59)
    md = random.randint(0, 59)
    hi = random.randint(8, 16)
    hd = random.randint(0, 2)
    if hd == 0:
        md = random.randint(1, 59)
    diffinsec = ((hd*3600)+(md*60))
    d = (Vm*diffinsec)/1000
    now = datetime.datetime(2000, 1, 1, hi, mi)
    tdiff = datetime.timedelta(hours=hd, minutes=md)
    then = str(now + tdiff)
    now = str(now)
    tdiff = str(tdiff)
    print("Uma pessoa que saiu de casa {} às {} horas chegou ao seu destino às {}. Sabendo que a distância percorrida por essa pessoa foi de {}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?".format(Transporte_escolhido, now[11:16], then[11:16], d))
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print("A resposta correta era {}. Tente novamente!".format(Vm))
if Transporte_escolhido == "ônibus":
    Vm = random.randint(12, 22)
    mi = random.randint(0, 59)
    md = random.randint(0, 59)
    hi = random.randint(8, 16)
    hd = random.randint(0, 6)
    if hd == 0:
        md = random.randint(1, 59)
    diffinsec = ((hd*3600)+(md*60))
    d = (Vm*diffinsec)/1000
    now = datetime.datetime(2000, 1, 1, hi, mi)
    tdiff = datetime.timedelta(hours=hd, minutes=md)
    then = str(now + tdiff)
    now = str(now)
    tdiff = str(tdiff)
    print("Uma pessoa que acabou de sair de uma estação de {} às {} horas chegou ao seu destino às {}. Sabendo que a distância percorrida por essa pessoa foi de {}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?".format(Transporte_escolhido, now[11:16], then[11:16], d))
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print("A resposta correta era {}. Tente novamente!".format(Vm))
if Transporte_escolhido == "bicicleta":
    Vm = random.randint(2, 6)
    mi = random.randint(0, 59)
    md = random.randint(0, 59)
    hi = random.randint(8, 16)
    hd = random.randint(0, 2)
    if hd == 0:
        md = random.randint(1, 59)
    diffinsec = ((hd*3600)+(md*60))
    d = (Vm*diffinsec)/1000
    now = datetime.datetime(2000, 1, 1, hi, mi)
    tdiff = datetime.timedelta(hours=hd, minutes=md)
    then = str(now + tdiff)
    now = str(now)
    tdiff = str(tdiff)
    print("Uma pessoa que saiu de casa com sua {} às {} horas chegou ao seu destino às {}. Sabendo que a distância percorrida por essa pessoa foi de {}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?".format(Transporte_escolhido, now[11:16], then[11:16], d))
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print("A resposta correta era {}. Tente novamente!".format(Vm))
if Transporte_escolhido == "motocicleta":
    Vm = random.randint(10, 30)
    mi = random.randint(0, 59)
    md = random.randint(0, 59)
    hi = random.randint(8, 16)
    hd = random.randint(0, 4)
    if hd == 0:
        md = random.randint(1, 59)
    diffinsec = ((hd*3600)+(md*60))
    d = (Vm*diffinsec)/1000
    now = datetime.datetime(2000, 1, 1, hi, mi)
    tdiff = datetime.timedelta(hours=hd, minutes=md)
    then = str(now + tdiff)
    now = str(now)
    tdiff = str(tdiff)
    print("Uma pessoa que saiu de casa com sua {} às {} horas chegou ao seu destino às {}. Sabendo que a distância percorrida por essa pessoa foi de {}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?".format(Transporte_escolhido, now[11:16], then[11:16], d))
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print("A resposta correta era {}. Tente novamente!".format(Vm))
if Transporte_escolhido == "skate":
    Vm = random.randint(1, 4)
    mi = random.randint(0, 59)
    md = random.randint(0, 59)
    hi = random.randint(8, 16)
    hd = random.randint(0, 2)
    if hd == 0:
        md = random.randint(1, 59)
    diffinsec = ((hd*3600)+(md*60))
    d = (Vm*diffinsec)/1000
    now = datetime.datetime(2000, 1, 1, hi, mi)
    tdiff = datetime.timedelta(hours=hd, minutes=md)
    then = str(now + tdiff)
    now = str(now)
    tdiff = str(tdiff)
    print("Uma pessoa que saiu de casa com seu {} às {} horas chegou ao seu destino às {}. Sabendo que a distância percorrida por essa pessoa foi de {}Km, qual a velocidade média, em metros por segundo, da pessoa no trajeto?".format(Transporte_escolhido, now[11:16], then[11:16], d))
    R = input(print("Qual é a sua resposta? "))
    Vm = str(Vm)
    Vm = Vm + "m/s"
    if Vm == R:
        print("Boa! Você acertou!!!")
    else:
        print("A resposta correta era {}. Tente novamente!".format(Vm))
