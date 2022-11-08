arr=[]
x=0
rows, cols=4,5
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(x)
        x += 1
    arr.append(col)
print(arr)
print(arr[1][2])