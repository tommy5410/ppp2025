
def gugudan(dan):
    for i in range(1,10):
        print(f"{dan}*{i}={dan * (i)}")
def main():
    dan = int(input("원하는 구구단의 단을 입력하세요 => "))
    gugudan(dan)

if __name__ == "__main__":
    main()       

