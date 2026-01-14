diem = []

while True:
    x = float(input("Nhập điểm (0 để dừng): "))
    if x == 0:
        break
    diem.append(x)

print("Danh sách điểm:", diem)

tb = sum(diem) / len(diem)
print("Điểm trung bình:", tb)

print("Điểm cao nhất:", max(diem))
