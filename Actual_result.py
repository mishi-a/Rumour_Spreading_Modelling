from matplotlib import pyplot as plt

x = []
y = []

data = []
set1 = set()
with open("/home/darkmatter/Documents/Network/data/higgs-activity_time.txt", "r") as myfile:
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
    y.append(len(set1)/279379)
    c_x = c_x + 1


for i in range(len(x)):
    print (x[i],y[i])

plt.plot(x,y)
plt.show()