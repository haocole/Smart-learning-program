def tinh_luong():
    hour = float(input("Nhập số giờ làm: "))
    rate = float(input("Nhập số lương giờ: "))
    if hour > 40:
        total_salary = 40 * rate + (hour - 40) * rate * 1.5
    else:
        total_salary = hour * rate
    print(f'Tống lưởng là: {total_salary}')