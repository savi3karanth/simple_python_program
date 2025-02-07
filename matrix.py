rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        x = int(input("Enter the elements: "))
        row.append(x)
    matrix.append(row)

print(matrix)