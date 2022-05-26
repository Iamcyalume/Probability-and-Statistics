import matplotlib.pyplot as plt
import random

arr = [0, 0, 0, 0, 0, 0, 0]
count = [10, 50, 100, 500, 1000, 10000, 100000, 1000000, 10000000, 200000000, 250000000]
pctg = [0, 0, 0, 0, 0, 0, 0]
math_pctg = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

for i in range(0, 12):
    for j in range(count[i]):
        arr[random.randint(1, 6)] += 1

    for h in range(1, 7):
        pctg[h] = float(arr[h])/float(count[i])

    arr = [0, 0, 0, 0, 0, 0, 0]
    
    if count[i]<=500:
        axis_range = [1, 6, 0, 1]

    elif count[i] >= 1000 and count[i] <= 10000:
        axis_range = [1, 6, 0, 0.3]

    elif count[i] >= 100000 and count[i] <=10000000:
        axis_range = [1, 6, 0.16, 0.17]

    else:
        axis_range = [1, 6, 0.16650, 0.16680]

    print(pctg)

    plt.figure(figsize = (5, 5))
    plt.axis(axis_range)

    plt.title('number of trials: %d' % count[i])

    plt.plot(math_pctg, 'g', label = 'mathematical probability')
    plt.plot(pctg, 'b-')
    plt.plot(pctg, 'ro', label = 'statistical probability')

    plt.legend()
    plt.show()
