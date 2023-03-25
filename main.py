import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 70]
Computer = [60, 100]
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']
x = np.arange(2) 
width = 0.15
fig, ax = plt.subplots()
# ******************************
# Make your code
# ax.bar(x-width*1.5, Math, width)
b1 = ax.bar(x-width*1.5, Math, width)
b2 = ax.bar(x-width*.5, English, width)
b3 = ax.bar(x-width*-.5, Physics, width)
b4 = ax.bar(x-width*-1.5, Computer, width)

ax.legend(labels, loc="lower center")
ax.set_title("Grouped graph for scores")
ax.bar_label(b1)
ax.bar_label(b2)
ax.bar_label(b3)
ax.bar_label(b4)
ax.set_xticks(x + width, names)

plt.show()
# ******************************


fig.savefig('A11.png')
