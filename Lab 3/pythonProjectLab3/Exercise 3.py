import random

n = int(input("Nhập số giá trị n: "))
X = []
Y = []
for i in range(n):
    X.append(random.randint(1, 100)) # Thêm giá trị ngẫu nhiên vào X

print("Danh sách X:", X)

count = 0
for i in range(n):
if X[i] % 2 != 0:
Y.append(X[i]) # Thêm giá trị lẻ vào danh sách Y
count += 1

if count == 0:
print("Không có số lẻ nào.")
else:
print("Danh sách Y:", Y)