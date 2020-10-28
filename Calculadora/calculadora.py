import math
class Calculadora:
    def __init__(self,A,B,C=0):
        self.A = A
        self.B = B
        self.C = C         

    def CalcularExpressao(self):
        R = (self.A + self.B)**2
        S = (self.B + self.C)**2
        D = (R+S)/2
        return D
    
    def Somar(self):
        soma=  self.A + self.B + self.C
        return soma
    def Subtrair(self):
        subtracao = self.A - self.B - self.C
        return subtracao

    def Bhaskara(self):
        
        result = []
        delta = (self.B**2)-4*(self.A*self.C)
      
        if delta>=0:
            raiz = math.sqrt(delta)          
            x1 = (-(self.B)+raiz) / (2*self.A)        
            x2 = (-(self.B)-raiz)/(2*(self.A))
            result.append(x1);
            result.append(x2);
            return result
        else:
            result.append("Sem valor real")
            return result

    
    


    