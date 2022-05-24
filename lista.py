import randVm as vm

nr_versoes = 2
nr_exercicios = 4
nr_listas = 10


def complet_rand(x = nr_listas, y = nr_exercicios):
    """
    Gera um número de listas completamente randomicamente
    Cada lista terá um conjunto diferente de exercícios, cada um com
    valores randomizados
    """
    for _ in range(x):
        lista = list()
        for _ in range(y):
            ex = vm.mru()
            ex.rand()
            lista.append(ex.texto)
        # TODO: Escrever a lista

def lista_simples(x = nr_exercicios):
    """
    Gera uma lista para ser utilizada várias vezes
    Os valores são gerados randomicamente mas o resultado é apenas uma lista
    """
    lista = list()
    for _ in range(x):
        ex = vm.mru()
        ex.rand()
        lista.append(ex.texto)
    # TODO: Escrever os exercicios em um arquivo.... ou retornar num print?

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
            x.renovar()
            res.append(x.rand())
        # TODO: Escrever a lista

print('teste')
