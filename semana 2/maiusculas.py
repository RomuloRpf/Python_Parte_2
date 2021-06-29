def maiusculas(frase):
    string = ""
    for i in frase:
        codigo = ord(i)
        if (codigo >= 65) and (codigo <= 90):
            string = string + i
    
    return string