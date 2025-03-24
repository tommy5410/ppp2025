import math
circle_r = int(input("반지름이 몇cm입니까?=>"))
circle_area = math.pi*(math.pow(circle_r,2))

print("반지름이 {}인 원의 면적은 {}입니다.".format(circle_r, circle_area))