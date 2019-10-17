# seq = [2, 4, 5, 13, 8, 5, 4, 1, 13, 5, 8, 4, 2, 5, 4, 1]
seq = [1, 3, 4, 7, 6, 4, 3, 6, 8, 3, 4, 1, 8, 3, 4, 9, 8]
linhas = 4


def fifo(seq, linhas):
    cash = [None] * linhas
    indicador = 0
    hit = 0
    miss = 0
    for bloco in seq:
        if bloco in cash:
            hit += 1
        else:
            cash[(indicador % linhas)] = bloco
            indicador += 1
            miss += 1
    print('FIFO')
    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('-----------------------')

def lru(seq, linhas):
    cash = [None] * linhas
    tempo = [0] * linhas
    hit = 0
    miss = 0
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
            cash[linha] = bloco
            for i in range(linhas):
                tempo[i] += 1
            tempo[linha] = 0
    print('LRU')
    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('-----------------------')

def lfu(seq, linhas):
    cash = [None] * linhas
    frequencia = [0] * linhas
    hit = 0
    miss = 0
    for bloco in seq:
        if bloco in cash:
            hit += 1
            linha = cash.index(bloco)
            frequencia[linha] += 1
        else:
            miss += 1
            linha = frequencia.index(min(frequencia))
            cash[linha] = bloco
            frequencia[linha] = 1
    print('LFU')
    print('cash ' + str(cash))
    print('hit = %d' % hit)
    print('miss = %d' % miss)
    print('-----------------------')


fifo(seq, linhas)
lru(seq, linhas)
lfu(seq, linhas)
