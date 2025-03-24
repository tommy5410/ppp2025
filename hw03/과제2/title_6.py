import math
x1 = int(input("x1좌표를 입력하세요.=>"))
x2 = int(input("x2좌표를 입력하세요.=>"))
y1 = int(input("y1좌표를 입력하세요.=>"))
y2 = int(input("y2좌표를 입력하세요.=>"))
distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print("x1좌표가 {} x2좌표가{}이고 y1좌표가{} y2좌표가{}일때 두 지점의 거리는{}입니다.".format(x1,x2,y1,y2,distance))