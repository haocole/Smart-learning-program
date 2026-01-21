import os
import sys

# 1.  CÁC HÀM CHỨC NĂNG 

def xem_lich(): 
    while True:
        xoa_va_ve_tieu_de("Xem so ngay trong thang")
        # 1. Kiểm tra nhập Tháng
        while True:
            try:
                thang = int(input(" Mời bạn nhập tháng (1-12): "))
                if 1 <= thang <= 12:
                    break # Tháng đúng thì thoát vòng lặp nhập tháng
                else:
                    print(" Lỗi: Tháng phải nằm trong khoảng từ 1 đến 12!")
            except ValueError:
                print(" Lỗi: Vui lòng nhập số nguyên cho tháng!")


        # 2. Kiểm tra nhập Năm
        while True:
            try:
                nam = input("Nhập năm (phải > 0, đủ 4 chữ số): ")

        # Kiểm tra có phải số không
                if not nam.isdigit():
                    print("Lỗi: Vui lòng nhập số nguyên cho năm!")
                    continue

        # Kiểm tra đúng 4 chữ số
                if len(nam) != 4:
                    print("Lỗi: Năm phải có đúng 4 chữ số!")
                    continue
                nam = int(nam)
                
        # Kiểm tra > 0
                if nam <= 0:
                   print(" Lỗi: Năm phải là số dương!")
                   continue
                break  # Năm đúng thì thoát vòng lặp
            except ValueError:
                      print(" Lỗi: Vui lòng nhập số nguyên cho năm!")
        # 3. Logic tính toán số ngày
        # Kiểm tra năm nhuận trước
        la_nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

        if thang in [1, 3, 5, 7, 8, 10, 12]:
            kq = "31 ngày"
        elif thang in [4, 6, 9, 11]:
            kq = "30 ngày"
        else: # Đây là tháng 2
            kq = "29 ngày" if la_nam_nhuan else "28 ngày"

        # 4. Hiển thị kết quả
        dong_xanh(f" KET QUA: Thang {thang}/{nam} co {kq}")
        
        
        if input("\n Nhấn '1' để xem tháng khác, nhấn Enter để về MENU: ") != '1': 
            break

def tinh_luong_nv():
    while True:
        xoa_va_ve_tieu_de("Tinh luong nhan vien")
        try:
            # Chặn lương cơ bản âm
            while True:
                l = float(input(" Mời nhập lương cơ bản/giờ (phải > 0): "))
                if l > 0: break
                print(" Lỗi: Mức lương không thể bằng 0 hoặc âm!")

            # Chặn thời gian làm việc âm
            while True:
                t = float(input(" Mời nhập tổng số giờ làm việc (phải > 0): "))
                if t >= 0: break
                print(" Lỗi: Thời gian làm việc không thể là số âm!")

            # Tính toán
            tong = (l * 40 + (t - 40) * l * 1.5) if t > 40 else l * t
            dong_xanh(f" TONG LUONG NHAN DUOC: {tong:,.2f} VND")
            
        except ValueError:
            print(" Lỗi: Vui lòng nhập con số hợp lệ!")
        
        
        if input("\n Nhấn '1' để tiếp tục tính, nhấn Enter để về MENU: ") != '1': break

def sap_xep_luong_nv():
    while True:
        xoa_va_ve_tieu_de("Sap xep luong nhan vien")
        try:
            # Chặn số lượng nhân viên bậy bạ
            while True:
                sl = int(input(" Mời nhập số lượng nhân viên (ít nhất là 1): "))
                if sl > 0: break
                print(" Lỗi: Số lượng phải là số dương!")

            ds = []
            for i in range(sl):
                while True:
                    try:
                        luong = float(input(f" Mời nhập lương người {i+1}: "))
                        if luong >= 0:
                            ds.append(luong)
                            break
                        print(" Lỗi: Lương không được âm!")
                    except ValueError:
                        print(" Lỗi: Lương phải là con số!")

            # Bubble Sort (Giữ nguyên logic của bạn)
            for i in range(len(ds)-1):
                for j in range(len(ds)-i-1):
                    if ds[j] > ds[j+1]: ds[j], ds[j+1] = ds[j+1], ds[j]
            
            dong_xanh(f" Danh sách tăng dần: {ds}")
        except ValueError: print(" Lỗi hệ thống nhập liệu!")
        
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
        
        
        if input("\n Nhấn '1' để nhập tên khác, nhấn Enter để về MENU: ") != '1': break

def tinh_diem_hs():
    while True:
        xoa_va_ve_tieu_de("Tinh diem trung binh")
        try:
            while True:
                sl = int(input(" Nhập số lượng môn học (ít nhất là 1): "))
                if sl > 0: break
                print(" Lỗi: Số lượng môn phải lớn hơn 0!")

            t_diem = 0; t_heso = 0
            for i in range(sl):
                print(f"--- Môn {i+1} ---")
                while True:
                    d = float(input(f"  Nhập điểm (0-10): "))
                    if 0 <= d <= 10: break
                    print("  Lỗi: Điểm phải từ 0 đến 10!")
                
                while True:
                    h = float(input(f"  Nhập hệ số (1-3): "))
                    if 1 <= h <= 3: break
                    print("  Lỗi: Hệ số phải từ 1 đến 3!")
                
                t_diem += d * h
                t_heso += h
            
            dong_xanh(f" DIEM TRUNG BINH: {t_diem/t_heso:.2f}")
        except ValueError: print(" Lỗi: Vui lòng nhập số!")
        
        if input("\n Nhấn '1' để tính cho học sinh khác, nhấn Enter để về MENU: ") != '1': break

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
# 3. VÒNG LẶP ĐIỀU KHIỂN CHÍNH (MENU)
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Vẽ bảng Menu chính
        dong_xanh("______________________________________________________________")
        dong_xanh("|************************************************************|")
        dong_xanh("|        ***** CHUONG TRINH HOC THONG MINH  *****            |")         
        dong_xanh("|************************************************************|")
        dong_xanh("|                                                            |")
        dong_xanh("|======================= MENU ===============================|")
        dong_xanh("| 1. Xem lich                                                |")
        dong_xanh("| 2. Tinh luong                                              |")
        dong_xanh("| 3. Xem luong (Sap xep)                                     |")
        dong_xanh("| 4. Xem thong tin nhan vien                                 |")
        dong_xanh("| 5. Tinh diem cua hoc sinh                                  |")
        dong_xanh("| 6. Thoat chuong trinh                                      |")
        dong_xanh("|************************************************************|")
        dong_xanh("|____________________________________________________________|")

        chon = input(WHITE + "\n Mời nhập lựa chọn (1-6): " + RESET)

        if chon == '1': xem_lich()
        elif chon == '2': tinh_luong_nv()
        elif chon == '3': sap_xep_luong_nv()
        elif chon == '4': in_ho_ten()
        elif chon == '5': tinh_diem_hs()
        elif chon == '6':
            print("\n  Tam biệt! Cảm ơn bạn đã sử dụng chương trình.")
            sys.exit()
        else:
            print(" Lựa chọn không hợp lệ!")
            input(" Nhấn Enter để chọn lại...")

if __name__ == "__main__":
   main()