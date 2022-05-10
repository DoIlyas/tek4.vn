my_str = input("Inter your string: ")

dem = 1

for i in range(len(my_str)):
    if my_str[i] == ' ':
        dem += 1

print(f'Have {dem} words.')