a = int(input("Nhập một số nguyên: "))
b = int(input("Nhập một số nguyên khác: "))
c = int(input("Nhập một số nguyên khác nữa: "))
if a > b and a > c:
    print(f"{a} là số lớn nhất.")
elif b > a and b > c:
    print(f"{b} là số lớn nhất.")
else:
    print(f"{c} là số lớn nhất.")
    