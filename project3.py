import os

# Bật chế độ hiển thị màu cho Terminal Windows
os.system("")

BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong(text):
    """In dòng chữ với nền màu xanh bao phủ toàn bộ chiều rộng thiết lập"""
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def dayOfMonth(thang):
    """Hàm xử lý logic xác định số ngày trong tháng"""
    if thang > 0 and thang <= 12:
        # Các tháng có 31 ngày
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            return ' 31 ngày'
        # Các tháng có 30 ngày
        elif thang in [4, 6, 9, 11]:
            return ' 30 ngày'
        # Xử lý riêng cho tháng 2 và năm nhuận
        else:
            nam = int(input(' Nhập năm: '))
            if (nam % 400 == 0) and (nam % 4 == 0 or nam % 100 != 0):
                return ' 29 ngày'
            else:
                return ' 28 ngày'
    else:
        return ' tháng không hợp lệ'

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Giao diện khung tiêu đề màu xanh
        dong("************************************************************")
        dong("            CHUC NANG: XEM SO NGAY TRONG THANG              ")
        dong("************************************************************")
        dong("")

        try:
            # Nhập tháng từ người dùng
            t = int(input(" Mời bạn nhập tháng cần xem: "))
            ket_qua = dayOfMonth(t)
            
            # Hiển thị kết quả trong khung xanh
            dong("")
            dong(f" KET QUA: {ket_qua}")
            dong("")
            dong("************************************************************")
            
        except ValueError:
            print(" Lỗi: Vui lòng nhập vào một số nguyên!")

        # Câu hỏi xác nhận tiếp tục theo yêu cầu của bạn
        print("\n Bạn có muốn tiếp tục chương trình không?")
        hoi = input(" Nhấn phím '1' để xem tháng tiếp theo, nhấn 'Enter' để thoát: ")
        
        # Nếu người dùng không nhập '1' (bao gồm cả việc chỉ nhấn Enter), chương trình sẽ thoát
        if hoi != '1':
            print(" Đang thoát chương trình xem lịch...")
            break

if __name__ == "__main__":
    main()