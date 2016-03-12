#!/usr/bin/python

"""
Used to track my 7 week pushup regime
"""

import matplotlib.pyplot as plt
import numpy as np

filename = "pushups.dat"

f = open(filename, 'r')
    
new_data = int(input("Pushups Completed: "))
data = [0] + [int(x) for x in f.read().split('\n')[:-1]]
f.close()
f = open(filename, 'a')

if new_data != -1:
    data.append(new_data)
    f.write(str(new_data) + '\n')

f.close()

xmin = 1
xmax = len(data)
ymin = 0
ymax = max(data)+10

plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel('Day')
plt.ylabel('Pushups')
plt.title('Pushups Tracker')
plt.grid(True)
plt.plot(data, linestyle='-', linewidth=2.0)
plt.show()
