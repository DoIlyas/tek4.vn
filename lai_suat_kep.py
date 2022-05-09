"""
Công thức tính lãi kép hàng năm có dạng là:

A=P∗(1+r/n)**nt

Trong đó:

A: Giá trị của tổng số tiền trong tương lai.
P: Số tiền gốc (đầu tư ban đầu).
r: Lãi suất danh nghĩa hàng năm.
n: Số lần ghép lãi trong một năm (nếu theo tháng sẽ là 12 lần, theo quý là 4 lần, hoặc nửa năm là 2 lần...)
t: Số năm tiền được gửi.
"""

prompt = "> "

print("Số tiền gốc:")
p = int(input(prompt))

print("Lãi suât hàng năm:")
r = float(input(prompt))

print("Số lần ghép lãi trong một năm:")
n = int(input(prompt))

print("Số năm gửi tiền:")
t = int(input(prompt))

a = p * (1 + (r/n))**(n*t)

print(f'Tổng số tiền là: {a}')