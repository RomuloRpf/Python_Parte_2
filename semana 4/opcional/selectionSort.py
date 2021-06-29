def ordena(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        menor_posicao = i
        for j in range(i+1,tamanho):
            if lista[j] < lista[menor_posicao]:
                menor_posicao = j
        lista[i],lista[menor_posicao] = lista[menor_posicao], lista[i]
    return lista
