from calculadora import Calculadora

newCalculadora1 = Calculadora(1,5)
print(newCalculadora1.Subtrair())
print(newCalculadora1.Somar())

calculadoraForExpression = Calculadora(3,-7,4)
print(calculadoraForExpression.CalcularExpressao())
resultado = calculadoraForExpression.Bhaskara()

i = 0
for x in resultado:
    i+=1
    print("x"+str(i))
    print(x);