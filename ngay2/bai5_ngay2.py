import random

so_ngau_nhiên = random.randint(1, 100)
nhap_so_cua_ban = int(input("Hãy đoán một số nguyên từ 1 đến 100: "))
while True:
    if nhap_so_cua_ban < so_ngau_nhiên:
        print("Số bạn đoán nhỏ hơn số ngẫu nhiên.")
        nhap_so_cua_ban = int(input("Hãy đoán lại: "))
    elif nhap_so_cua_ban > so_ngau_nhiên:
        print("Số bạn đoán lớn hơn số ngẫu nhiên.")
        nhap_so_cua_ban = int(input("Hãy đoán lại: "))
    else:
        print("Chúc mừng! Bạn đã đoán đúng số ngẫu nhiên.")
        break