#Graficar 
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-5,5,100)
y = x**3 
plt.plot(x,y, "g.-", label = "x3", linewidth = 6)
plt.title("funcion cubica")
plt.legend
plt.grid()
plt.show()