hoten=input("Ho ten: ")
ngaycong=int(input("So ngay cong: "))
dongia=int(input("Don gia ngay cong: "))
hesophucap=float(input("He so phu cap: "))
tamung=int(input("Tam ung: "))
luong=dongia*ngaycong*hesophucap
thuclinh=luong-tamung
print("Nhan vien ",hoten,", Co tien Luong=",luong,", Tam ung=",tamung," va Thuc linh=",thuclinh,sep="")