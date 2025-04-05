def is_leap_year(y):
      leap_year = False
      if y % 4 == 0:
            if y % 100 == 0:
                  if y % 400 == 0:
                        print(f"{y}는 윤년입니다.")
                  else: 
                       print(f"{y}는 평년입니다.")
            else:
                  print(f"{y}는 윤년입니다.")
      else:
            print(f"{y}는 평년입니다.")
      return leap_year
def main ():
      want_year = int(input("원하는 연도를 입력하세요 =>"))
      is_leap = is_leap_year(want_year)
      print(f"윤년 여부: {is_leap}")
if __name__ == "__main__":
    main()
          
      