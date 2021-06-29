def encontra_impares(lista):
    tamanho = len(lista) - 1
    if tamanho < 0:
        return []
    else:
        if (lista[tamanho] % 2) != 0:
            impar = []
            impar.extend(encontra_impares(lista[0:tamanho]))
            impar = impar + [lista[tamanho]]
            return impar
        else:
            return encontra_impares(lista[0:tamanho])
