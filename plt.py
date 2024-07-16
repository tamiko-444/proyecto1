#Graficar 
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-4,5,100)
y = x**3 
plt.plot(x,y,"r.-", label = "x3", linewidth = 3)
plt.title("funcion cubica")
plt.legend()
plt.grid()
plt.show()
