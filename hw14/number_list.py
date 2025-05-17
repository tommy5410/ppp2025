def main():
    numbers = []
    while True:
        x = input("X=? ")
        if x == '-1':
            break
        try:
            num = int(x)
            if num > 0:
                numbers.append(num)
            # 0 이하의 정수는 무시
        except ValueError:
            # 정수로 변환 불가(문자 등)는 무시
            continue

    print(f"입력된 값은 {numbers} 입니다.", end=' ')
    print(f"총 {len(numbers)}개의 자연수가 입력되었고,", end=' ')
    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"평균은 {avg}입니다.")
    else:
        print("평균은 계산할 수 없습니다.")

if __name__ == "__main__":
    main()