# 과제 복습해보기 
#3
calories = {"블루베리":0.43,"체리":0.57,"오렌지":0.47}
eat_blueberry = int(input("블루베리를 먹은양을 입력하세요"))
eat_cherry = int(input(" 체리를 먹은양을 입력하세요"))
eat_orange = int(input("오렌지를 먹은양을 입력하세요"))
total_calories = calories["블루베리"]*eat_blueberry+calories["체리"]*eat_cherry+calories["오렌지"]*eat_orange
print(f"총섭취한 칼로리는 : {total_calories}")