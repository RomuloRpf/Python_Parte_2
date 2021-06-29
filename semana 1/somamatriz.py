def soma_matrizes(m1, m2):
    linhas = len(m1)
    colunas= len(m1[0])
    if linhas != len(m2):
        return False
    elif colunas != len(m2[0]):
        return False
    
    matriz = []
    for i in range(linhas):
        line = []
        for j in range(colunas):
            elemento = m1[i][j] + m2[i][j]
            line.append(elemento)
        matriz.append(line)
    
    return matriz