prompt = "> "


# tạo List từ bán phím
try:
    print("- Nhập số phần tử của mảng:")
    n = int(input(prompt))
    if n <= 0:
        exit()
except:
    print("Phải nhập số nguyên!")
    exit()

my_list = []

for i in range(n):
    my_list.append(input(prompt + f'Nhập phần tử thứ {i + 1}: '))

print("List vừa tạo (str): ", my_list)


# ép str sang int trong my_list
my_list_int = []

for i in my_list:
    my_list_int.append(int(i))

print("List vừa tạo (int):", my_list_int)


# chèn số nguyên e vào vị trí i
e = int(input(prompt + "Nhập e: "))
i = int(input(prompt + "Nhập i: "))
print("- Chèn số nguyên e vào vị trí i:")
my_list_int.insert(i, e)
print(my_list_int)


# xoá lần đầu tiên xuất hiện của e
print("- Xoá lần đầu tiên xuất hiện của số e:")
my_list_int.remove(e)
print(my_list_int)


# chèn số nguyên e vào cuối danh sách
print("- Chèn số nguyên e vào cuối danh sách:")
my_list_int.append(e)
print(my_list_int)


# sắp xếp danh sách
print("- Sắp xếp danh sách:")
my_list_int.sort()
print(my_list_int)


# lấy phần tử cuối cùng
print("- Phần tử cuối cùng là:")
print(my_list_int.pop())


# đảo ngược danh sách
print("- Đảo ngược danh sách:")
my_list_int.reverse()
print(my_list_int)