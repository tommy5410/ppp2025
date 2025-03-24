import math
bmi_weight = int (input("무게가얼마인가요?=>"))
bmi_height = int(input("키가얼마인가요?=>")) /100
bmi = bmi_weight / (math.pow(bmi_height,2))
print("키가{}무게가{}면, bmi는{}입니다.".format(bmi_height,bmi_weight,bmi))
if 24.9>=bmi>=23 :  
    print(f"키가{bmi_height}무게가{bmi_weight}면, bmi는{bmi}이며 이는 비만 전단계입니다.")     # and를 웬만하면 쓰기
elif 29.9>=bmi>=25 :
     print(f"키가{bmi_height}무게가{bmi_weight}면, bmi는{bmi}이며 이는 1 단계 비만입니다.")
elif 34.9>=bmi>=30 :
     print(f"키가{bmi_height}무게가{bmi_weight}면, bmi는{bmi}이며 이는 2 단계 비만입니다.")
elif bmi>=35 :
     print(f"키가{bmi_height}무게가{bmi_weight}면, bmi는{bmi}이며 이는 3 단계 비만입니다.")
else :
     print(f"키가{bmi_height}무게가{bmi_weight}면, bmi는{bmi}이며 이는 비만이 아닙니다.")