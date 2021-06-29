def insertion_sort(lista):

    lista_ordenada = [0] + lista[:]
    tamanho = len(lista_ordenada)
    
    for i in range(2,tamanho):
        sentinela = lista_ordenada[i]
        lista_ordenada[0] = sentinela
        j = i
        while lista_ordenada[j-1] > sentinela:
            lista_ordenada[j] = lista_ordenada[j-1]
            j -=1
        lista_ordenada[j] = sentinela
        
    return lista_ordenada[1:]

def insertion_alt(lista):

    tamanho = len(lista)
    
    for i in range(1,tamanho):
        sentinela = lista[i]
        j = i
        while (lista[j-1] > sentinela) and (j > 0):
            lista[j] = lista[j-1]
            j -=1
        lista[j] = sentinela
        
    return lista
