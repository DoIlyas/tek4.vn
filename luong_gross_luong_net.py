"""
Lương Net = Lương Gross - (BHXH + BHYT + BHTN) - Thuế TNCN (nếu có)
Trong đó, tổng các khoản BHXH + BHYT + BHTN là 10.5% của tổng lương.

Còn thuế TNCN sẽ được tính dựa trên thu nhập sau khi đã giảm trừ các khoản sau:
- Giảm trừ gia cảnh đối với chính bản thân: 11 triệu đồng/tháng.
- Giảm trừ người phụ thuộc: 4,4 triệu đồng/tháng/người.
- Các khoản đóng bảo hiểm bắt buộc, quỹ hưu trí tự nguyện, đóng góp từ thiện.
-------------------
Thuế thu nhập cá nhân phải nộp = Thu nhập tính thuế x Thuế suất
Trong đó:
- Thu nhập tính thuế = Thu nhập chịu thuế - Các khoản giảm trừ
- Thu nhập chịu thuế = Tổng thu nhập - Các khoản được miễn
Căn cứ theo công thức nêu trên, mức thuế thu nhập cá nhân từ tiền lương, tiền công bạn phải nộp như sau:
- Xác định thu nhập chịu thuế: 25 triệu đồng;
- Các khoản giảm trừ:
+ Mức giảm trừ gia cảnh cho bản thân và người nhà lần lượt là: 11 triệu đồng và 4,4 triệu đồng.
+ BHXH, BHYT, BHTN: 25 x10,5% = 2,625 triệu đống
=> Tổng khoản giảm trừ = 2,625 + 11 + 4,4 = 18,025 triệu đồng
- Tính thu nhập tính thuế = 25 - 18,025 = 6,975 triệu đồng
Như vậy, do bạn có thu nhập tính thuế/tháng từ trên 5 đến 10 triệu đồng nên thuế suất từ tiền lương, tiền công là 10% (Bậc thuế 2).
=> Thuế thu nhập cá nhân phải nộp = 6,975 x 10% - 0,25 trđ = 447.500 đồng
"""
title = "CHƯƠNG TRÌNH TÍNH THUẾ THCN, LƯƠNG NET"
print('\n')
print(title.center(100, '-'))
prompt = '> '

print("Nhập vào mức lương của bạn (triệu đồng):")
luong_gross = float(input(prompt))
print("Nhập số người phụ thuộc:")
giam_tru_phu_thuoc = int(input(prompt))

bao_hiem = luong_gross * 0.105
tong_khoan_giam_tru = bao_hiem + 11 + 4.4
thu_nhap_tinh_thue = luong_gross - tong_khoan_giam_tru

if giam_tru_phu_thuoc <= 0 or thu_nhap_tinh_thue < 0:
    print("\nBạn không phải đóng thuế TNCN.")
    print(f'Khoản bảo hiểm bạn phải đóng: {bao_hiem} triệu đồng.')
    print(f'Số tiền lực nhận của bạn (Lương Net): {luong_gross - bao_hiem} triệu đồng')
else:
    if 0 < thu_nhap_tinh_thue <= 5:
        thue_tncn = thu_nhap_tinh_thue * 0.05
        print(f'Thuế TNCN bậc 1, đóng: {thue_tncn} triệu đồng.')
        print(f'Số tiền lực nhận của bạn (Lương Net): {luong_gross - bao_hiem- thue_tncn} triệu đồng')
    elif 5 < thu_nhap_tinh_thue <= 10:
        thue_tncn = thu_nhap_tinh_thue * 0.1
        print(f'Thuế TNCN bậc 2, đóng: {thue_tncn} triệu đồng.')
        print(f'Số tiền lực nhận của bạn (Lương Net): {luong_gross - bao_hiem - thue_tncn} triệu đồng')
    elif 10 < thu_nhap_tinh_thue <= 18:
        thue_tncn = thu_nhap_tinh_thue * 0.15
        print(f'Thuế TNCN bậc 3, đóng: {thue_tncn} triệu đồng.')
        print(f'Số tiền lực nhận của bạn (Lương Net): {luong_gross - bao_hiem - thue_tncn} triệu đồng')
    elif 18 < thu_nhap_tinh_thue <= 32:
        thue_tncn = thu_nhap_tinh_thue * 0.2
        print(f'Thuế TNCN bậc 4, đóng: {thue_tncn} triệu đồng.')
        print(f'Số tiền lực nhận của bạn (Lương Net): {luong_gross - bao_hiem - thue_tncn} triệu đồng')

