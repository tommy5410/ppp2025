def get_range_list(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    return numbers   
def main():
    n = int(input("출력을 원하는 숫자를 입력하세요"))
    total_num = get_range_list(n)
    print(total_num)

if __name__ == "__main__":
    main()
