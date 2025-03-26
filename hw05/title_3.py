fruit_cal = {"블루베리":0.43,"체리":0.57,"오렌지":0.47}
fruit_eat ={"블루베리":150, "체리" :200, "오렌지": 300}
fruit_eat_list = ["블루베리","체리","오렌지"]
total = 0
for item in fruit_eat_list:
     total= total + (fruit_cal[item] * fruit_eat[item])             
print(f"총 칼로리는 {total}kcal입니다") 