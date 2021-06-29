def ordenada(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        if lista[i] > lista[i+1]:
            return False
    return True
