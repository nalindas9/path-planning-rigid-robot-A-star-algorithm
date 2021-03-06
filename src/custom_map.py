"""
Map Definition for A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Plotting the final map

u=150.     #x-position of the center
v=100.    #y-position of the center
a=40.     #radius on the x-axis
b=20.    #radius on the y-axis

fig = plt.figure()
plt.axes()
circle = plt.Circle((225, 150), radius=25, fill=False)
line1 = plt.Line2D((0, 300), (200, 200), lw=1)
line2 = plt.Line2D((0, 300), (0, 0), lw=1)
line3 = plt.Line2D((0, 0), (0, 200), lw=1)
line4 = plt.Line2D((300, 300), (0, 200), lw=1)

# Lines for the diamond
line5 = plt.Line2D((200, 225), (30, 45), lw=1)
line6 = plt.Line2D((225, 250), (45, 30), lw=1)
line7 = plt.Line2D((250, 225), (30, 15), lw=1)
line8 = plt.Line2D((225, 200), (15, 30), lw=1)

# Lines for the tilted cuboid
line9 = plt.Line2D((95,  100), (30, 38.66), lw=1)
line10 = plt.Line2D((100, 35.05), (38.66, 76.16), lw=1)
line11 = plt.Line2D((35.05, 30.05), (76.16, 67.5), lw=1)
line12 = plt.Line2D((30.05, 95), (67.5, 30), lw=1)

# Lines for the concave shape
line13 = plt.Line2D((20,  25), (120, 185), lw=1)
line14 = plt.Line2D((25, 75), (185, 185), lw=1)
line15 = plt.Line2D((75, 100), (185, 150), lw=1)
line16 = plt.Line2D((100, 75), (150, 120), lw=1)
line17 = plt.Line2D((75,  50), (120, 150), lw=1)
line18 = plt.Line2D((50, 20), (150, 120), lw=1)


plt.gca().add_line(line1)
plt.gca().add_line(line2)
plt.gca().add_line(line3)
plt.gca().add_line(line4)
plt.gca().add_line(line5)
plt.gca().add_line(line6)
plt.gca().add_line(line7)
plt.gca().add_line(line8)
plt.gca().add_line(line9)
plt.gca().add_line(line10)
plt.gca().add_line(line11)
plt.gca().add_line(line12)
plt.gca().add_line(line13)
plt.gca().add_line(line14)
plt.gca().add_line(line15)
plt.gca().add_line(line16)
plt.gca().add_line(line17)
plt.gca().add_line(line18)
plt.gca().add_patch(circle)
plt.axis('scaled')

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
plt.grid(color='lightgray',linestyle='--')
