def main() :
    calories = {"블루베리":0.43,"체리":0.57,"오렌지":0.47}   # 사전 사용
    total_cal = 0
    fruit_eat_list = ["블루베리","체리","오렌지"]
    for item in fruit_eat_list: 
        fruit_eat = int(input(f"{item}을 먹은 양을 입력하세요=>"))
        total_cal += calories[item]* fruit_eat
    print(f"총 칼로리는{total_cal :.2f}입니다.") 
if __name__ == "__main__":
    main()

    


