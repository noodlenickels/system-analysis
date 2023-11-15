import csv
import numpy as np

def task(data):
    
    matrix = np.array([[float(num) for num in row] for row in data])
   
    n, k = matrix.shape

    entropy = 0
    for j in range(n):
        for i in range(k):
            lij = matrix[j, i]
            if lij != 0: 
                print(lij / (n - 1))
                entropy -= (lij / (n - 1)) * np.log2(lij / (n - 1))

    return round(entropy, 1)

with open('task3/example.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

print(task(data))