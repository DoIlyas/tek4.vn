n = int(input("Number of rows: "))

for i in range(n):
    for j in range(n - i):
        print(end=' ')
    for z in range(i + 1):
        print('*', end=' ')
    print()