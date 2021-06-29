def conta_letras(frase, contar = "vogais"):
    string = frase.lower()
    vogal = 0
    espacos = 0
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vogal += 1
        elif i==' ':
            espacos += 1
    if contar == "vogais":
        return vogal
    elif contar == "consoantes":
        return (len(frase) - vogal - espacos)