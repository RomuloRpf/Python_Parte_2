def menor_nome(nomes):
    menor = nomes[0].strip()
    for i in nomes:
        nome = i.strip()
        if len(nome) < len(menor):
            menor = nome
    
    return menor.capitalize()