class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c
    
    def perimetro(self):
        return (self.a + self.b + self.c)
        
    def tipo_lado(self):
        if (self.a == self.b) and (self.b == self.c):
            return "equilátero"
            
        elif (self.a == self.b) or (self.a == self.c) or(self.b == self.c):
            return "isósceles"
            
        else:
            return "escaleno"
    
    def retangulo(self):
        lados = [self.a,self.b,self.c]
        lados.sort()
        a,b,c = lados[2]**2, lados[1]**2,lados[0]**2
        if a == (b + c):
            return True
        
        return False
    
    def semelhantes(self, triangulo):
        t1 = [self.a,self.b,self.c]
        t2 = [triangulo.a,triangulo.b,triangulo.c]
        t1.sort()
        t2.sort()
        if (t1[0] % t2[0] != 0) and (t2[0] % t1[0] != 0):
            return False
        elif (t1[1] % t2[1] != 0) and (t2[1] % t1[1] !=0):
            return False
        elif (t1[2] % t2[2] != 0) and (t2[2] % t1[2] !=0):
            return False
        
        return True