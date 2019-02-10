#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math
ts = 8000
x = np.arange(ts)
y = np.sin(2 * math.pi * 1 * x/ts)
plt.plot(x,y)
plt.plot(x,y)
plt.xlabel('Sample')
plt.ylabel('Voltage')
plt.show() 
