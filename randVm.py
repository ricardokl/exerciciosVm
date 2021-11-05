import random as rd
import datetime 

#criando lista de transporte
t = rd.choice(["carro" , "ônibus"])
#criando função das varivaveis
def variaveis(vmin = 20 , vmax = 100):
    vm= rd.randint(vmin, vmax)
    tempo = rd.randint(0,55)
    d = vm*tempo
    hinicial = (datetime.timedelta())
    hfinal = (datetime.timedelta())
    return vm, d, hinicial, hfinal


#criando um exercicio para teste(perguntar ao ricardo oq fazer para conseguir utilizar o timedelta de maneira eficaz.)
if t == "ônibus":
    vm , d , hinicial , hfinal = variaveis()
    print(f'um {t} saí do seu posto às {hinicial[0:5]} horas e chega na cidade às {hfinal[0:5]}, sabendo que em todo seu percurso, o {t} teve uma velocidade constante de {vm}km, calcule a distancia entre o posto e a cidade.')
