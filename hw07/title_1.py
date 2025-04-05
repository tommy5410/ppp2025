def average(nums):
    avg= sum(nums) / len(nums)
    return avg
def main ():
    num_list = [ 2,5,9,4,26,51,31,62,54]
    average_sum = average(num_list)
    print(f"리스트의 평균은 {average_sum:.2f}입니다.")

if __name__ == "__main__":
    main()