import os
import sys

# Bật màu cho Windows console
os.system("")

BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong(text):
    # Hàm này giúp in một dòng có nền xanh trải dài hết chiều rộng WIDTH
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def hien_thi_giao_dien():
    os.system('cls' if os.name == 'nt' else 'clear')
    dong("************************************************************")
    dong("        ***** CHUONG TRINH HOC THONG MINH  ***** ")
    dong("************************************************************")
    dong("")
    dong("=============== MENU ===============================")
    dong("")
    dong("Xin vui long chon:")
    dong("1. Xem lich")
    dong("2. Tinh luong")
    dong("3. Xem luong")
    dong("4. Xem thong tin nhan vien")
    dong("5. Tinh diem cua hoc sinh")
    dong("6. Thoat chuong trinh")
    dong("")
    dong("************************************************************")

def main():
    while True:
        hien_thi_giao_dien()
        
        try:
            # Nhập lựa chọn từ người dùng theo logic ảnh mẫu
            a = int(input(WHITE + "Mời nhập lựa chọn: " + RESET))
            
            if 0 < a < 6:
                if a == 1:
                    thang = int(input('Mời nhập tháng: '))
                    # print(tinhToan.dayOfMonth(thang))
                    print(f"-> Đang xử lý xem lịch tháng {thang}...")
                    
                elif a == 2:
                    luong = float(input('Mời nhập lương: '))
                    time = float(input('Mời nhập thời gian làm việc: '))
                    # print(tinhToan.tinhLuong(luong, time))
                    print(f"-> Lương tính toán được là: {luong * time}")
                    
                elif a == 3:
                    so_luong = int(input('Mời nhập số lượng nhân viên cần xem lương: '))
                    # tinhToan.sapXepLuong(so_luong)
                    print(f"-> Đang hiển thị bảng lương cho {so_luong} nhân viên...")
                    
                elif a == 4:
                    # tinhToan.print_name()
                    print("-> Đang hiển thị thông tin nhân viên...")
                    
                elif a == 5:
                    soLuongMon = int(input('Nhập số lượng môn học: '))
                    # print(tinhToan.tinhDiemTrungBinh(soLuongMon))
                    print(f"-> Đang tính điểm trung bình cho {soLuongMon} môn...")

                # Hỏi xem có muốn tiếp tục không
                hoi = input('Bạn có muốn tiếp tục chương trình không? y/n: ')
                if hoi.lower() == 'n': # Sửa lại logic một chút để 'n' là thoát
                    break
            
            elif a == 6:
                print("Đang thoát chương trình...")
                sys.exit() # Sử dụng thư viện sys để thoát
            
            else:
                print("Lựa chọn không hợp lệ (0 < a < 6)!")
                break

        except ValueError:
            print("Vui lòng chỉ nhập số!")
        
        input("\nNhấn Enter để quay lại Menu...")

if __name__ == "__main__":
    main()