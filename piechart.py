import matplotlib.pyplot as plt
x = [55,45]
mylabels = ['Principal', 'Interest']
myexplode = [0.0,0.1]
plt.pie(x, labels=mylabels, autopct='%1.1f%%',explode=myexplode)
plt.show()