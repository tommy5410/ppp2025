def text2list(txt):
    txt_list = txt.split()
    nums = []                                           
    for num_text in txt_list:                           
        nums.append(int(num_text))
    return nums
def average(nums):
    return sum(nums)/len(nums)
def median(nums):
    print(sorted(nums))
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list)//2]

def read_text(filename):
    text = ""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(f"!{line.strip()}!")
            text += " "+ line.strip()
    return text

def read_numbers(filename):
    nums = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
    return nums

def main():
    text = read_text("numbers3.txt")
    nums = text2list(text)
    print(nums)
    print(f"총 숫자의 개수는 {len(nums)}개 입니다")
    print(f"평균값은 {average(nums):.1f}입니다")
    print(f"최댓값은 {max(nums)}입니다")
    print(f"최솟값은 {min(nums)}입니다")
    print(f"중앙값은 {median(nums)}입니다")
if __name__ == "__main__":
    main()