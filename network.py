# importing the required module
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math
import random


def func2(x, y, tk, n, lamda):
    za = n / 279379
    for i in x:
        z = 1 - ((1 - za) * math.exp(-1 * lamda * (i - tk)))
        y.append(z)


x = []
tk = 1341100972
lim = 1341214200 - tk
# lim = lim/3600
for a in range(tk):
    if a * 60 <= lim:
        x.append(tk + a * 60)
    else:
        break

'''for i in x:
    print(i)'''
y = []
lamda = 8.8e-9
func2(x, y, tk, 1, lamda)
x1 = []
y1 = []
tk = x[-1]
lim = 1341253799 - tk
for a in range(tk):
    if a * 60 <= lim:
        x1.append(tk + a * 60)
    else:
        break
func2(x1, y1, tk, 3655, lamda)
x.extend(x1)
y.extend(y1)
print(y[-1])
x1 = []
y1 = []
tk = x[-1]
lim = 1341368999 - tk
for a in range(tk):
    if a * 60 <= lim:
        x1.append(tk + a * 60)
    else:
        break
lamda = 0.0000009
func2(x1, y1, tk, 9573, lamda)
# print(len(x),len(x1),len(y),len(y1))
x.extend(x1)
y.extend(y1)
print(y[-1])
x1 = []
y1 = []
tk = x[-1]
lim = 1341705593 - tk
for a in range(tk):
    if a * 60 <= lim:
        x1.append(tk + a * 60)
    else:
        break
lamda = 0.00006
func2(x1, y1, tk, 32927, lamda)
x.extend(x1)
y.extend(y1)
print(y[-1])
# func2(x,y,tk,6176)
# func2(x,y,tk,25326)
'''for i in y:
    print(i)'''

'''cmap = colors.ListedColormap(['white', 'red'])
bounds=[1341214200]
norm = colors.BoundaryNorm(bounds, cmap.N)'''
plt.plot(x, y)

# plt.xlim(xmax=10000+tk)
# plt.ylim(ymax=0.001)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
