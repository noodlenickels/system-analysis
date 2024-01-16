import numpy as np
import json

# Создание массива и запись в файл
matrix = [[1, 2, 3, 4, 5], [5, 2, 3, 1, 4], [2, 5, 3, 4, 1], [4, 1, 5, 3, 2], [3, 1, 5, 2, 4]]
np.savetxt('matrix.csv', matrix, delimiter=',', fmt='%d')
print('Matrix saved successfully', '\n')

# Чтение из csv файла
csv_data = np.genfromtxt('example.csv', delimiter=',')
print(csv_data, '\n')

# Чтение json
with open('example.json') as file:
    json_data = json.load(file)
    print(json_data)