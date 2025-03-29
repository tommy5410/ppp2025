def sum_n(n):
    Sum = 0
    for i in range(1,n+1):
        Sum += i
    return Sum

def main():
    n = int(input("원하는 숫자를 입력하세요: "))
    total_sum= sum_n(n)
    print(total_sum)

if __name__ == "__main__":
    main()  