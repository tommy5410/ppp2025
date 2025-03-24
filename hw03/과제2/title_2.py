import math
bmi_weight = int(input("무게가얼마인가요?=>"))
bmi_height = int(input("키가얼마인가요?=>")) /100
bmi = bmi_weight / (math.pow(bmi_height,2))
print("키가{}무게가{}면, bmi는{}입니다.".format(bmi_height,bmi_weight,bmi))