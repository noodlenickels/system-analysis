import csv

def task(data):
    
    matrix = []
    for i in range(6):
        matrix.append([0, 0, 0, 0, 0, 0])
    for i in data:
        matrix[int(i[0])-1][int(i[1])-1] = 1
        matrix[int(i[1])-1][int(i[0])-1] = -1

    # непосредственное управление
    r1 = []
    for i in range(len(matrix)):
        for v in matrix[i]:
            if v == 1: 
                r1.append(i+1)
                break

    # непосредственное подчинение
    r2 = []
    for i in range(len(matrix)):
        for v in matrix[i]:
            if v == -1: 
                r2.append(i+1)
                break
            
    # опосредственное управление
    r3 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                for el in matrix[j]:
                    if el == 1:
                        r3.append(i+1)
                        break
    
    # опосредственное подчинение
    r4 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                for el in matrix[j]:
                    if el == -1:
                        r4.append(i+1)
                        break
            
    # соподчинение
    r5 = []
    for i in range(len(matrix)):
        if matrix[i].count(1) > 1:
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    r5.append(j+1)
                    
    return [r1, r2, r3, r4, r5]

with open('task2/example.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

print(task(data))