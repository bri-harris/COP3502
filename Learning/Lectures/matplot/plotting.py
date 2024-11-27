import matplotlib.pyplot as plt

with open('data.txt') as file:
    data = []
    for l in file:
        data.append(float(l))

with open('data_2.txt') as file:
    data_2 = []
    for l in file:
        data_2.append(float(l))

years = range(2005, 2016)

plt.plot(years, data, 'ro-', linewidth=1, markersize=3, label='Math scores')
plt.plot(years, data_2, 'bx-', linewidth=1, markersize=3, label='Verbal scores')

plt.legend(shadow=True, loc='upper right')
plt.xlabel('Year')
plt.ylabel('Score')
plt.title("Florida SAT Scores")

plt.show()




