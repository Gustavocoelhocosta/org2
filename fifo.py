import random as re


def aleatorio(seq, linhas):
    cash = [None] * linhas
    hit = 0
    miss = 0
    sub = 0
    for bloco in seq:
        if bloco in cash:
            hit += 1
        else:
            linha = re.randrange(linhas)
            if cash[linha]:
                sub += 1
            cash[linha] = bloco
            miss += 1
    print('ALEATORIO')
    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('sub = %d' % sub)
    print('-----------------------')



def fifo(seq, linhas):
    cash = [None] * linhas
    indicador = 0
    hit = 0
    miss = 0
    sub = 0
    for bloco in seq:
        if bloco in cash:
            hit += 1
        else:
            if cash[(indicador % linhas)]:
                sub += 1
            cash[(indicador % linhas)] = bloco
            indicador += 1
            miss += 1
    print('FIFO')
    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('sub = %d' % sub)
    print('-----------------------')

def lru(seq, linhas):
    print('LRU')
    cash = [None] * linhas
    tempo = [0] * linhas
    hit = 0
    miss = 0
    sub = 0
    for bloco in seq:
        if bloco in cash:
            hit += 1
            tempo = list(map(lambda x: x + 1, tempo))
            linha = cash.index(bloco)
            tempo[linha] = 0
        else:
            miss += 1
            linha = tempo.index(max(tempo))
            if cash[linha]:
                sub += 1
            cash[linha] = bloco
            tempo = list(map(lambda x: x + 1, tempo))
            tempo[linha] = 0

    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('sub = %d' % sub)
    print('-----------------------')

def lfu(seq, linhas):
    cash = [None] * linhas
    frequencia = [0] * linhas
    hit = 0
    miss = 0
    sub = 0
    for bloco in seq:
        if bloco in cash:
            hit += 1
            linha = cash.index(bloco)
            frequencia[linha] += 1
        else:
            miss += 1
            linha = frequencia.index(min(frequencia))
            if cash[linha]:
                sub += 1
            cash[linha] = bloco
            frequencia[linha] = 1
    print('LFU')
    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('sub = %d' % sub)
    print('-----------------------')


def algoritimo_substituicao(seq, linhas):
    print('-----------------------')
    seq = list(map(int, seq.split(", ")))
    if linhas >=2 and linhas <= 256:
        aleatorio(seq, linhas)
        fifo(seq, linhas)
        lru(seq, linhas)
        lfu(seq, linhas)
    else:
        print('numero de linhas da cach incorreta')



# seq = open('acesso2.txt', 'r').readline()[0:-1]

seq = open(input('entre com o nome do arquivo '), 'r').readline()[0:-1]
linhas = int(input('entre com o numero de linhas da cach '))


algoritimo_substituicao(seq, linhas)
seq = open(input('ENTER para sair '), 'r').readline()[0:-1]




