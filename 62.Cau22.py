GiaNiemYet=int(input("Nhap Gia niem yet: "))
ChietKhau=int(input("Nhap Chiet khau: "))
VAT=(GiaNiemYet-ChietKhau)*0.01
GiaBan=GiaNiemYet-ChietKhau+VAT
print("Gia ban: ",GiaBan)