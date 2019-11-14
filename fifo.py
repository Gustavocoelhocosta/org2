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
            for i in range(linhas):
                tempo[i] += 1
            linha = cash.index(bloco)
            tempo[linha] = 0
        else:
            miss += 1
            linha = tempo.index(max(tempo))
            if cash[linha]:
                sub += 1
            cash[linha] = bloco
            for i in range(linhas):
                tempo[i] += 1
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
    seq = seq.split(', ')
    if linhas >=2 and linhas <= 256:
        aleatorio(seq, linhas)
        fifo(seq, linhas)
        lru(seq, linhas)
        lfu(seq, linhas)
    else:
        print('numero de linhas da cach incorreta')


# seq = '3890, 3751, 0, 3751, 3751, 35, 64, 133, 0, 1, 2, 3, 4, 5, 6, 6, 4, 1000, 1001, 1002, 1003, 1004, 1004, 1005, 1006, 1007, 0, 6, 6, 4, 1000, 1001, 1002, 1003, 1004, 1004, 1005, 1006, 1007, 3890, 3751, 0, 6, 6, 4, 1000, 1001, 1002, 1003, 1004, 1004, 1005, 1006, 1007'
# linhas = 20

seq = input('entre com a sequência ')
linhas = int(input('entre com o número de linhas da cash '))
algoritimo_substituicao(seq, linhas)


