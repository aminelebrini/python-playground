
import math

X1 = float(input("enter X1 : "))
X2 = float(input("enter X2 : "))

Y1 = float(input("enter Y1 : "))
Y2 = float(input("enter Y2 : "))

x_calcul = math.pow(X2 - X1, 2)
y_calcul = math.pow(Y2 - Y1, 2)

result = math.sqrt(x_calcul + y_calcul)

print(f"the distance is : {result:.2f}")