import os

# Cấu hình màu sắc giao diện
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    """In dòng chữ trên nền màu xanh bao phủ toàn bộ chiều rộng"""
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def tinhDiemTrungBinh(soLuongMonHoc):
    """
    Logic tính điểm trung bình có hệ số từ dự án mẫu.
    Bao gồm vòng lặp kiểm tra tính hợp lệ của điểm và hệ số.
    """
    tongdiem_heso = 0
    tongheso = 0
    
    for i in range(1, soLuongMonHoc + 1):
        # Nhập và kiểm tra điểm (phải từ 0 đến 10)
        diem = float(input(f" Nhập điểm của môn học {i} (0-10): "))
        while diem < 0 or diem > 10:
            print(" Điểm phải nằm trong khoảng 0-10. Vui lòng nhập lại.")
            diem = float(input(f" Nhập điểm của môn học {i} (0-10): "))
            
        # Nhập và kiểm tra hệ số (chỉ nhận các giá trị: 1, 1.5, 2, 2.5, 3)
        heso = float(input(f" Nhập hệ số của môn học {i} (1, 1.5, 2, 2.5, 3): "))
        while heso not in (1, 1.5, 2, 2.5, 3):
            print(" Hệ số chỉ nằm trong các giá trị: 1, 1.5, 2, 2.5, 3. Vui lòng nhập lại.")
            heso = float(input(f" Nhập hệ số của môn học {i} (1, 1.5, 2, 2.5, 3): "))
            
        tongdiem_heso += diem * heso
        tongheso += heso
    
    # Tính điểm trung bình cuối cùng
    dtb = tongdiem_heso / tongheso
    
    # Hiển thị kết quả trong khung xanh
    print("")
    dong_xanh(" KET QUA HOC TAP:")
    dong_xanh(f" Tổng số hệ số đã nhập: {tongheso}")
    dong_xanh(f" Điểm trung bình là: {dtb:.2f}")

def main_tinh_diem():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Giao diện tiêu đề khung xanh
        dong_xanh("************************************************************")
        dong_xanh("            CHUC NANG: TINH DIEM TRUNG BINH                 ")
        dong_xanh("************************************************************")
        dong_xanh("")

        try:
            sl = int(input(" Nhập số lượng môn học: "))
            if sl > 0:
                tinhDiemTrungBinh(sl)
                dong_xanh("")
                dong_xanh("************************************************************")
            else:
                print(" Số lượng môn học phải lớn hơn 0!")
        except ValueError:
            print(" Lỗi: Vui lòng nhập số nguyên hợp lệ!")

        # Vòng lặp hỏi tiếp tục hoặc thoát về menu chính
        print("\n Bạn có muốn tính điểm cho học sinh khác không?")
        hoi = input(" Nhấn phím '1' để tiếp tục, nhấn 'Enter' để thoát: ")
        
        if hoi != '1':
            print(" Đang quay lại menu chính...")
            break

if __name__ == "__main__":
    main_tinh_diem()