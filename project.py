import os
import sys

# 1. Cấu hình giao diện màu sắc
os.system("") # Bật màu cho Windows
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

# 2. Định nghĩa các hàm chức năng (Logic từ ảnh mẫu)

def dayOfMonth(thang):
    """Hàm xem lịch"""
    if 0 < thang <= 12:
        if thang in [1, 3, 5, 7, 8, 10, 12]: return ' 31 ngày'
        elif thang in [4, 6, 9, 11]: return ' 30 ngày'
        else:
            nam = int(input(' Nhập năm: '))
            if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0): return ' 29 ngày'
            else: return ' 28 ngày'
    return ' tháng không hợp lệ'

def tinhLuong(luong, time):
    """Hàm tính lương"""
    tong = 0.0
    if time > 40 and luong > 0:
        tong = (luong * 40) + (luong * (time - 40) * 1.5)
    elif 0 < time <= 40:
        tong = luong * time
    return tong

def sapXepLuong(soLuong):
    """Hàm sắp xếp lương"""
    ds = []
    for i in range(1, soLuong + 1):
        ds.append(float(input(f" Nhập lương người {i}: ")))
    n = len(ds)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ds[j] > ds[j + 1]:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]
    print(f" Danh sách tăng dần: {ds}")

def print_name():
    """Hàm in họ tên"""
    full_name = input(" Nhập họ và tên: ").strip()
    name_parts = full_name.split()
    if len(name_parts) < 2: return print("Vui lòng nhập đủ họ tên!")
    print(f" Họ và tên đệm: {' '.join(name_parts[:-1]).title()}")
    print(f" Tên: {name_parts[-1].title()}")

def tinhDiemTrungBinh(soLuong):
    """Hàm tính điểm"""
    tong_diem = 0; tong_he_so = 0
    for i in range(1, soLuong + 1):
        diem = float(input(f" Nhập điểm môn {i}: "))
        he_so = float(input(f" Nhập hệ số môn {i}: "))
        tong_diem += diem * he_so
        tong_he_so += he_so
    dtb = tong_diem / tong_he_so
    return f" Điểm trung bình: {dtb:.2f}"

# 3. Vòng lặp Menu chính để quay lại được bảng màu xanh
def main():
    while True:
        # Hiển thị bảng Menu
        os.system('cls' if os.name == 'nt' else 'clear')
        dong_xanh("************************************************************")
        dong_xanh("      ****** Chuong Trinh Hoc Thong Minh ******* ")
        dong_xanh("************************************************************")
        dong_xanh("")
        dong_xanh("======================== MENU ==============================")
        dong_xanh(" Xin vui long chon :")
        dong_xanh(" 1. Xem lich")
        dong_xanh(" 2. Tinh luong")
        dong_xanh(" 3. Xem luong (Sap xep)")
        dong_xanh(" 4. Xem thong tin nhan vien")
        dong_xanh(" 5. Tinh diem cua hoc sinh")
        dong_xanh(" 6. Thoat chuong trinh")
        dong_xanh("************************************************************")

        chon = input("\n Mời nhập lựa chọn: ")

        # Điều hướng chức năng
        if chon == '1':
            t = int(input(" Nhập tháng: "))
            print(dayOfMonth(t))
        elif chon == '2':
            l = float(input(" Nhập lương: ")); time = float(input(" Nhập giờ: "))
            print(f" Tổng lương: {tinhLuong(l, time)}")
        elif chon == '3':
            sl = int(input(" Nhập số lượng nhân viên: "))
            sapXepLuong(sl)
        elif chon == '4':
            print_name()
        elif chon == '5':
            sl = int(input(" Nhập số môn học: "))
            print(tinhDiemTrungBinh(sl))
        elif chon == '6':
            print(" Đang thoát...")
            sys.exit()

        # Sau mỗi chức năng, hỏi để quay lại Menu
        print("\n" + "-"*30)
        hoi = input(" Nhấn phím '1' để tiếp tục chức năng vừa rồi, phím khác để quay lại MENU: ")
        if hoi != '1':
            continue # Quay lại đầu vòng lặp while để hiện Menu

if __name__ == "__main__":
    main()