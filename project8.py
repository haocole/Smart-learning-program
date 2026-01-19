import sys
import os

# Cấu hình màu sắc giao diện
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def exitChuongTrinh(lua_chon = '6'):
    """
    Hàm thoát chương trình lấy chính xác từ logic dự án mẫu.
    Sử dụng sys.exit() để dừng chương trình ngay lập tức.
    """
    import sys
    if lua_chon == '6':
        print("")
        dong_xanh("************************************************************")
        dong_xanh("          BAN DA DUNG CHUONG TRINH. TAM BIET!               ")
        dong_xanh("************************************************************")
        print(RESET)
        sys.exit() # Thoát chương trình