import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
plt.style.use('fivethirtyeight')
 
x_val = []
y_val = []
 
index = count()
 
def graphAnimation(i):
    x_val.append(next(index))
    y_val.append(random.randint(0,5))
    plt.cla()
    plt.plot(x_val, y_val)
 
ani = FuncAnimation(plt.gcf(), graphAnimation, interval = 10)

 
 
plt.tight_layout()
plt.show()
