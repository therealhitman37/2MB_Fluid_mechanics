'''
The problem
Would a tank of radius = 5 m, and height = 10 m be overfilled if the influx of water is 15 m3/min within two hours?
'''

from math import pi
import numpy as np
import matplotlib.pyplot as plt

# definitions:
r = 5                     # radius, (m)
h = 10                    # height, (m)
Q = 15                    # flow rate (m^3/min)
pi = 3.14159              # or use from math import pi

# Volume of the tank
V_tank = pi * r**2 * h

t = 120 # time, (min)

# Volume of water flowing in
V_in = Q * t

def func():
    if V_in > V_tank:
        print("Tank overfilled by " + str(V_in - V_tank) + " m^3")
    else:
        print("Safe")

# func()

t = np.arange(0,120)

plt.figure(figsize=(8,6))
plt.plot(t,Q*t,'--')
plt.plot([0,120],[V_tank,V_tank])
plt.xlabel('$t$ (min)',fontsize=18)
plt.ylabel('$V$ (m$^3$/min)',fontsize=18)
plt.legend((r'$V_f$',r'$V_{\mathrm{tank}}$'),fontsize=16)

plt.show()