import os

# Thiết lập màu sắc và định dạng giao diện
BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"
WIDTH = 60

def dong_xanh(text):
    """Hàm in dòng chữ trên nền xanh bao phủ toàn bộ chiều rộng"""
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

def sapXepLuong(soLuong):
    """Logic sắp xếp lương lấy chính xác từ mã nguồn mẫu"""
    ds = []
    # Nhập danh sách lương
    for i in range(1, soLuong + 1):
        luong = float(input(f" Mời nhập lương của người thứ {i}: "))
        ds.append(luong)
    
    # Thuật toán sắp xếp nổi bọt (Bubble Sort)
    n = len(ds)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ds[j] > ds[j + 1]:
                # Hoán đổi vị trí
                temp = ds[j]
                ds[j] = ds[j + 1]
                ds[j + 1] = temp
    
    # Hiển thị kết quả trong khung xanh
    print("")
    dong_xanh(" KET QUA SAP XEP:")
    dong_xanh(f" Danh sách lương theo thứ tự tăng dần: {ds}")

def chuc_nang_sap_xep_luong():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Hiển thị giao diện tiêu đề
        dong_xanh("************************************************************")
        dong_xanh("               CHUC NANG: SAP XEP LUONG                     ")
        dong_xanh("************************************************************")
        dong_xanh("")

        try:
            sl = int(input(" Mời nhập số lượng nhân viên cần xem lương: "))
            if sl > 0:
                sapXepLuong(sl)
                dong_xanh("")
                dong_xanh("************************************************************")
            else:
                print(" Số lượng phải lớn hơn 0!")
                
        except ValueError:
            print(" Lỗi: Vui lòng nhập số nguyên hợp lệ!")

        # Vòng lặp hỏi tiếp tục hoặc thoát
        print("\n Bạn có muốn thực hiện sắp xếp lại không?")
        hoi = input(" Nhấn phím '1' để tiếp tục, nhấn 'Enter' để thoát: ")
        
        if hoi != '1':
            print(" Đang quay lại menu chính...")
            break

if __name__ == "__main__":
    chuc_nang_sap_xep_luong()