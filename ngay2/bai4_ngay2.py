nhap = int(input("Nhập một số nguyên: "))
# tong cac so tu 1 den nhap
tong = 0
for i in range(1, nhap + 1):
    tong += i
print(f"Tổng các số từ 1 đến {nhap} là: {tong}")