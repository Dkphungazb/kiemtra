# Import thư viện
import math

# Khai báo biến toàn cục
PI = 3.14

# Định nghĩa hàm
def circle_area(radius):
    return PI * math.pow(radius, 2)

# Chương trình chính
if __name__ == "__main__":
    r = 5
    area = circle_area(r)
    print(f"Diện tích hình tròn có bán kính {r} là {area}")
