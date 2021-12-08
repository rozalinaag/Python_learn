"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы."""




mx = []
while True:
    row = input()
    if row == 'end':
        break
    mx.append(list(map(int, row.split())))

for i in range(len(mx)):
    for j in range(len(mx[0])):
        print(mx[i-1][j] + mx[(i+1)%len(mx)][j] + mx[i][j-1] + mx[i][(j+1)%len(mx[0])], end = " ")
    print("")





