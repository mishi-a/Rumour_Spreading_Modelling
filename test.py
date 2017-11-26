from matplotlib import pyplot as plt
import math

x1 = []
y1 = []


def func2(x, tk, lamda, n):
    za = n / 279379
    z = 1 - ((1 - za) * math.exp(-1 * lamda * (x - tk)))
    y1.append(z)


for i in range(1341100972, 1341214200):
    x1.append(i - 1341100972)
    func2(i, 1341100972, 8.8e-9, 1)

for i in range(1341214200, 1341253800):
    x1.append(i - 1341100972)
    func2(i, 1341214200, 8.8e-9, 3655)

for i in range(1341253800, 1341369000):
    x1.append(i - 1341100972)
    func2(i, 1341253800, 0.0000009, 9573)

for i in range(1341369000, 1341705593):
    x1.append(i - 1341100972)
    func2(i, 1341369000, 0.00002, 32927)

##################################

x = []
y = []

data = []
set1 = set()
with open("/home/darkmatter/Documents/Rumour_Spreading_Modelling/data/higgs-activity_time.txt", "r") as myfile:
    for words in myfile:
        words = words.strip()
        data.append(words)

start = 1341100972
i = 0
cnt = 0
c_x = 0

while i < len(data):
    val = data[i].split()
    ts = int(val[2])
    if start == ts:
        i = i + 1
        set1.add(val[0])
        j = i
        while j < len(data):
            n_val = data[j].split()
            if int(n_val[2]) == start:
                i = i + 1
                j = j + 1
                set1.add(n_val[0])
            else:
                break
        start = start + 1
    else:
        start = start + 1
    x.append(c_x)
    y.append(len(set1) / 279379)
    c_x = c_x + 1

for i in range(len(x)):
    print(x[i], y[i])

plt.plot(x, y, "r", label="Actual Result")
# plt.show()
# print(len(x1), len(y1))
plt.plot(x1, y1, "g", label="Estimated Result")

#plt.axhspan(0, 1, 0, 1341214200 - 1341100972, facecolor="b")

plt.xlabel("Time Passed after 1st july 2012 05:32:00 AM in (sec)")
# naming the y axis
plt.ylabel("Fraction Of user active at given time t ")
plt.legend()
plt.show()
