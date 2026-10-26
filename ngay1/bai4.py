nhap_so_giay = int(input("Nhập số giây: "))
gio = nhap_so_giay // 3600
phut = (nhap_so_giay % 3600) // 60
giay = nhap_so_giay % 60
print(f"{nhap_so_giay} giây tương đương với {gio} giờ, {phut} phút và {giay} giây.")