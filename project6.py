import os

# Thiết lập màu sắc giao diện
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    """In dòng chữ trên nền màu xanh bao phủ toàn bộ chiều rộng thiết lập"""
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def print_name():
    """
    Hàm xử lý họ tên lấy chính xác từ logic trong dự án mẫu.
    Sử dụng các phương thức xử lý chuỗi: strip, split, join và title.
    """
    # Nhập họ tên và loại bỏ khoảng trắng thừa ở hai đầu
    full_name = input(" Nhập họ và tên: ").strip()
    
    # Tách chuỗi thành danh sách các từ
    name_parts = full_name.split()
    
    # Kiểm tra tính hợp lệ (phải có ít nhất Họ và Tên)
    if len(name_parts) < 2:
        print(" Vui lòng nhập đầy đủ cả họ và tên!")
        return

    # Lấy phần họ và tên đệm (từ đầu đến sát cuối) và viết hoa chữ cái đầu
    ho_va_ten_dem = " ".join(name_parts[:-1]).title()
    
    # Lấy phần tên (từ cuối cùng) và viết hoa chữ cái đầu
    ten = name_parts[-1].title()
    
    # Tạo chuỗi họ tên đầy đủ đã được chuẩn hóa
    full_name_capitalized = full_name.title()

    # Hiển thị kết quả trong khung xanh cho đẹp
    print("")
    dong_xanh(" KET QUA XU LY TEN:")
    dong_xanh(f" Họ và tên đệm: {ho_va_ten_dem}")
    dong_xanh(f" Tên của bạn là: {ten}")
    dong_xanh(f" Tên đầy đủ của bạn là: {full_name_capitalized}")

def main_in_ten():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Hiển thị tiêu đề giao diện giống hình mẫu bạn gửi
        dong_xanh("************************************************************")
        dong_xanh("            CHUC NANG: IN HO VA TEN NHAN VIEN               ")
        dong_xanh("************************************************************")
        dong_xanh("")

        # Gọi hàm xử lý in tên
        print_name()
        
        dong_xanh("")
        dong_xanh("************************************************************")

        # Vòng lặp hỏi tiếp tục theo yêu cầu của bạn
        print("\n Bạn có muốn nhập tên nhân viên khác không?")
        hoi = input(" Nhấn phím '1' để tiếp tục, nhấn 'Enter' để thoát: ")
        
        if hoi != '1':
            print(" Đang quay lại menu chính...")
            break

if __name__ == "__main__":
    main_in_ten()