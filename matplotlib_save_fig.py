import matplotlib.pyplot as plt

data = [23,85, 72, 43, 52]
labels = ['A', 'B', 'C', 'D', 'E']
plt.xticks(range(len(data)), labels)
plt.xlabel('Class')
plt.ylabel('Amounts')
plt.title('I am title')
plt.bar(range(len(data)), data) 
plt.savefig('./files/plot.png')