def xem_lich():
    thang = int(input("Nhap thang: "))
    if thang in [1,3,5,7,8,10,12]:
        print("31 ngay")
    elif thang in [4,6,9,11]:
        print("30 ngay")
    elif thang == 2:
        print("28 hoac 29 ngay")
    else:
        print("Thang khong hop le")

xem_lich()
