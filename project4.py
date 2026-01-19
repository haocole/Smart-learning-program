import os

# Thiết lập màu sắc và định dạng giao diện
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    """Hàm bổ trợ để in dòng chữ trên nền xanh bao phủ toàn bộ chiều rộng"""
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def tinhLuong(luong, time):
    """Logic tính lương lấy chính xác từ mã nguồn mẫu"""
    tongluong = 0.0
    # Nếu làm trên 40 giờ thì tính lương tăng ca hệ số 1.5
    if time > 40 and luong > 0:
        tongluong = (luong * 40)
        timehon = time - 40
        tongluong = tongluong + (luong * timehon * 1.5)
    # Nếu làm dưới hoặc bằng 40 giờ
    elif time <= 40 and time > 0:
        tongluong = luong * time
    else:
        # Trường hợp nhập số âm
        if time < 0 or luong < 0:
            print(' Vui lòng nhập lại số dương!')
    return tongluong

def chuc_nang_tinh_luong():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Hiển thị giao diện khung xanh theo hình mẫu
        dong_xanh("************************************************************")
        dong_xanh("                CHUC NANG: TINH LUONG                       ")
        dong_xanh("************************************************************")
        dong_xanh("")

        try:
            # Nhập dữ liệu đầu vào
            l = float(input(" Mời nhập lương cơ bản (mỗi giờ): "))
            t = float(input(" Mời nhập thời gian làm việc (giờ): "))
            
            ket_qua = tinhLuong(l, t)
            
            # Hiển thị kết quả trong khung xanh
            dong_xanh("")
            dong_xanh(f" TONG LUONG NHAN DUOC: {ket_qua:,.2f}")
            dong_xanh("")
            dong_xanh("************************************************************")
            
        except ValueError:
            print(" Lỗi: Vui lòng nhập số hợp lệ!")

        # Vòng lặp hỏi tiếp tục hoặc thoát theo ý muốn của bạn
        print("\n Bạn có muốn tính lương cho người khác không?")
        hoi = input(" Nhấn phím '1' để tiếp tục, nhấn 'Enter' để thoát: ")
        
        # Nếu không nhấn '1' (nhấn Enter hoặc phím khác) thì thoát vòng lặp
        if hoi != '1':
            print(" Đang quay lại menu chính...")
            break

if __name__ == "__main__":
    chuc_nang_tinh_luong()