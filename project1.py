# Bat mau cho Windows
import os
os.system("")

BLUE = "\033[44m"
WHITE = "\033[97m"
RESET = "\033[0m"

WIDTH = 60

def dong(text):
    print(BLUE + WHITE + text.ljust(WIDTH) + RESET)

# ====== BAT DAU GIAO DIEN ======
dong("************************************************************")
dong("        *****  CHUONG TRINH HOC THONG MINH  *****           ")
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
