import math
circle_r = int(input("반지름이 몇cm입니까?=>"))
circle_area = math.pi*(math.pow(circle_r,2))
circumference = math.pi * circle_r * 2
print("반지름이 {}인 원의 둘레는 {:.1f}입니다".format(circle_r,circumference ))
print("반지름이 {}인 원의 넓이는 {:.2f}입니다".format(circle_r,circle_area ))