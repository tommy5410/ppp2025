def c2f(t_C):
    return (t_C * 9/5) + 32

temp_c = int(input("섭씨 온도를 입력하세요=>"))
temp_f = c2f(temp_c)
print(f"{temp_c}°C => {temp_f:.1f}°F")


if __name__ == "__main__":
        main()    