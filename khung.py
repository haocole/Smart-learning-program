# Vẽ phần tiêu đề trên cùng
#print("**************************************************")
#print("* Chuong Trinh Hoc Thong Minh             *")
#print("**************************************************")

# Vẽ thanh Menu
#print("====================== MENU ======================")

# Vẽ khung chứa các lựa chọn
#print("__________________________________________________")
#print("| Xin vui long chon :                            |")
#print("| 1. Xem lich                                    |")
#print("| 2. Tinh luong                                  |")
#print("| 3. Xem luong                                   |")
#print("| 4. Xem thong tin nhan vien                     |")
#print("| 5. Tinh diem cua hoc sinh                      |")
#print("| 6. Thoat chuong trinh                          |")
#print("|                                                |")
#print("|________________________________________________|")

import os
import sys

# 1. CẤU HÌNH GIAO DIỆN CHUNG
os.system("") # Kích hoạt màu cho Windows
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    """Tạo dòng chữ nền xanh trải dài hết chiều rộng"""
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def xoa_va_ve_tieu_de(ten_chuong):
    """Xóa màn hình và vẽ tiêu đề xanh cho từng chức năng"""
    os.system('cls' if os.name == 'nt' else 'clear')
    dong_xanh("************************************************************")
    dong_xanh(f"            CHUC NANG: {ten_chuong.upper()} ")
    dong_xanh("************************************************************")
    dong_xanh("")

# 2.  CÁC HÀM CHỨC NĂNG 

def xem_lich():
    while True:
        xoa_va_ve_tieu_de("Xem so ngay trong thang")
        try:
            thang = int(input(" Mời bạn nhập tháng cần xem: "))
            if 0 < thang <= 12:
                if thang in [1, 3, 5, 7, 8, 10, 12]: kq = "31 ngày"
                elif thang in [4, 6, 9, 11]: kq = "30 ngày"
                else:
                    nam = int(input(' Nhập năm: '))
                    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0): kq = "29 ngày"
                    else: kq = "28 ngày"
                dong_xanh(f" KET QUA: {kq}")
            else: print(" Tháng không hợp lệ!")
        except ValueError: print(" Lỗi: Vui lòng nhập số!")
        
        dong_xanh("************************************************************")
        if input("\n Nhấn '1' để xem tháng khác, nhấn Enter để về MENU: ") != '1': break

def tinh_luong_nv():
    while True:
        xoa_va_ve_tieu_de("Tinh luong nhan vien")
        try:
            l = float(input(" Mời nhập lương cơ bản (giờ): "))
            t = float(input(" Mời nhập thời gian làm việc: "))
            tong = (l * 40 + (t - 40) * l * 1.5) if t > 40 else l * t
            dong_xanh(f" TONG LUONG NHAN DUOC: {tong:,.2f}")
        except ValueError: print(" Lỗi nhập liệu!")
        
        dong_xanh("************************************************************")
        if input("\n Nhấn '1' để tiếp tục tính, nhấn Enter để về MENU: ") != '1': break

def sap_xep_luong_nv():
    while True:
        xoa_va_ve_tieu_de("Sap xep luong nhan vien")
        try:
            sl = int(input(" Mời nhập số lượng nhân viên: "))
            ds = [float(input(f" Mời nhập lương người {i+1}: ")) for i in range(sl)]
            # Bubble Sort
            for i in range(len(ds)-1):
                for j in range(len(ds)-i-1):
                    if ds[j] > ds[j+1]: ds[j], ds[j+1] = ds[j+1], ds[j]
            dong_xanh(f" Danh sách tăng dần: {ds}")
        except ValueError: print(" Lỗi nhập liệu!")
        
        dong_xanh("************************************************************")
        if input("\n Nhấn '1' để thực hiện lại, nhấn Enter để về MENU: ") != '1': break

def in_ho_ten():
    while True:
        xoa_va_ve_tieu_de("In ho va ten nhan vien")
        full_name = input(" Nhập họ và tên: ").strip()
        parts = full_name.split()
        if len(parts) >= 2:
            dong_xanh(f" Họ và tên đệm: {' '.join(parts[:-1]).title()}")
            dong_xanh(f" Tên của bạn là: {parts[-1].title()}")
        else: print(" Vui lòng nhập đầy đủ họ tên!")
        
        dong_xanh("************************************************************")
        if input("\n Nhấn '1' để nhập tên khác, nhấn Enter để về MENU: ") != '1': break

def tinh_diem_hs():
    while True:
        xoa_va_ve_tieu_de("Tinh diem trung binh")
        try:
            sl = int(input(" Nhập số lượng môn học: "))
            t_diem = 0; t_heso = 0
            for i in range(sl):
                d = float(input(f" Nhập điểm môn {i+1} (0-10): "))
                h = float(input(f" Nhập hệ số môn {i+1} (1-3): "))
                t_diem += d * h
                t_heso += h
            dong_xanh(f" DIEM TRUNG BINH: {t_diem/t_heso:.2f}")
        except ValueError: print(" Lỗi nhập liệu!")
        
        dong_xanh("************************************************************")
        if input("\n Nhấn '1' để tính cho học sinh khác, nhấn Enter để về MENU: ") != '1': break

# 3. VÒNG LẶP ĐIỀU KHIỂN CHÍNH (MENU)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Vẽ bảng Menu chính
        dong_xanh("************************************************************")
        dong_xanh("        ***** CHUONG TRINH HOC THONG MINH  ***** ")
        dong_xanh("************************************************************")
        dong_xanh("")
        dong_xanh("=============== MENU ===============================")
        dong_xanh(" 1. Xem lich")
        dong_xanh(" 2. Tinh luong")
        dong_xanh(" 3. Xem luong (Sap xep)")
        dong_xanh(" 4. Xem thong tin nhan vien")
        dong_xanh(" 5. Tinh diem cua hoc sinh")
        dong_xanh(" 6. Thoat chuong trinh")
        dong_xanh("************************************************************")

        chon = input(WHITE + "\n Mời nhập lựa chọn (1-6): " + RESET)

        if chon == '1': xem_lich()
        elif chon == '2': tinh_luong_nv()
        elif chon == '3': sap_xep_luong_nv()
        elif chon == '4': in_ho_ten()
        elif chon == '5': tinh_diem_hs()
        elif chon == '6':
            print("\n Đang thoát chương trình... Tạm biệt!")
            sys.exit()
        else:
            print(" Lựa chọn không hợp lệ!")
            input(" Nhấn Enter để chọn lại...")

if __name__ == "__main__":
    main()