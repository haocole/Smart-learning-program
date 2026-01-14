import os

# ================== TIỆN ÍCH ==================
def clear():
    os.system("cls")

def pause():
    input("\nNhan Enter de quay lai menu...")

# ================== CHỨC NĂNG 1 ==================
def days_in_month():
    clear()
    print("===== XEM LICH =====")
    thang = int(input("Nhap thang (1-12): "))

    if thang in [1,3,5,7,8,10,12]:
        print("Thang", thang, "co 31 ngay")
    elif thang in [4,6,9,11]:
        print("Thang", thang, "co 30 ngay")
    elif thang == 2:
        print("Thang 2 co 28 hoac 29 ngay")
    else:
        print("Thang khong hop le")

    pause()

# ================== CHỨC NĂNG 2 ==================
def tinh_luong():
    clear()
    print("===== TINH LUONG =====")
    gio = float(input("Nhap so gio lam: "))
    luong_gio = float(input("Nhap luong 1 gio: "))

    if gio <= 40:
        tong = gio * luong_gio
    else:
        tong = 40 * luong_gio + (gio - 40) * luong_gio * 1.5

    print("Tong tien luong:", tong)
    pause()

# ================== CHỨC NĂNG 3 ==================
def sap_xep_luong():
    clear()
    print("===== SAP XEP LUONG =====")
    n = int(input("Nhap so nhan vien: "))
    ds = []

    for i in range(n):
        ds.append(float(input(f"Luong nhan vien {i+1}: ")))

    ds.sort()
    print("Danh sach luong tang dan:", ds)
    pause()

# ================== CHỨC NĂNG 4 ==================
def xu_ly_ten():
    clear()
    print("===== THONG TIN NHAN VIEN =====")
    name = input("Nhap ten nhan vien: ").strip().lower()

    parts = name.split()
    parts = [p.capitalize() for p in parts]

    ho_lot = " ".join(parts[:-1])
    ten = parts[-1]
    full = " ".join(parts)

    print("Ho va ten lot:", ho_lot)
    print("Ten:", ten)
    print("Ho ten day du:", full)

    pause()

# ================== CHỨC NĂNG 5 ==================
def tinh_dtb():
    clear()
    print("===== TINH DIEM TRUNG BINH =====")
    so_mon = int(input("Tong so mon hoc: "))

    tong_diem = 0
    tong_he_so = 0

    for i in range(so_mon):
        while True:
            diem = float(input(f"Diem mon {i+1}: "))
            if 0 <= diem <= 10:
                break
            print("Nhap sai! Diem tu 0-10")

        he_so = float(input(f"He so mon {i+1}: "))

        tong_diem += diem * he_so
        tong_he_so += he_so

    dtb = tong_diem / tong_he_so

    print("So mon hoc:", so_mon)
    print("Tong he so:", tong_he_so)
    print("Diem trung binh:", round(dtb, 2))

    pause()

# ================== MENU ==================
def menu():
    print("*" * 43)
    print("****** CHUONG TRINH HOC THONG MINH ******")
    print("*" * 43)
    print("\n================ MENU ================")
    print("1. Xem lich")
    print("2. Tinh luong")
    print("3. Xem luong")
    print("4. Xem thong tin nhan vien")
    print("5. Tinh diem cua hoc sinh")
    print("6. Thoat")

# ================== CHƯƠNG TRÌNH CHÍNH ==================
os.system("color 1F")

while True:
    clear()
    menu()
