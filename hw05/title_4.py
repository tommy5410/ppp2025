import math
angle = int(input("구하고 싶은 각도를 입력하세요=> "))
start_angle = 0
total_angle = angle
for i in range( 0 , total_angle+1):
   radian =  math.radians(i)
   sin_value = math.sin(radian)
   cos_value = math.cos(radian)
   tan_value = math.tan(radian)
   print(f"각도가{i}°일떄,라디안은{radian:.4f},사인값은{sin_value:.4f},cos값은{cos_value:.4f},탄젠트값은{tan_value:.4f}입니다.")
     