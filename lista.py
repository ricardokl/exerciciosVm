import randVm as vm

nr_versoes = 2
nr_exercicios = 4
nr_listas = 10


def lista_simples(x = nr_exercicios):
    """
    Gera uma lista para ser utilizada várias vezes
    Os valores são gerados randomicamente mas o resultado é apenas uma lista
    """
    lista = list()
    for _ in range(x):
        ex = vm.mru()
        ex.rand()
        texto = ex.subs()
        lista.append(texto)
    print( "==========Lista==========" )
    for e in lista:
        print(e)

def complet_rand(x = nr_listas, y = nr_exercicios):
    """
    Gera um número de listas completamente randomicamente
    Cada lista terá um conjunto diferente de exercícios, cada um com
    valores randomizados
    """
    for _ in range(x):
        lista_simples(y)

def rand_valores(x = nr_exercicios, y = nr_versoes):
    """
    Escolhe exercicios randomicamente mas gera apenas 1 modelo
    O modelo então é usado para gerar várias versões com valores diferentes
    """
    lista = list()
    for _ in range(x):
        ex = vm.mru()
        lista.append(ex)
    for _ in range(y):
        res = list()
        for x in lista:
            x.rand()
            res.append(x.subs())
        print( "==========Lista==========" )
        for e in res:
            print(e)
