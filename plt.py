#Graficar 
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-5,5,100)
y = x**3 
plt.plot(x,y,"r--")
plt.title("funcion en python")

plt.grid()
plt.show()