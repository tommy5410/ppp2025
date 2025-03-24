x = int(input("x좌표를 입력하세요.=>"))
y = int(input("y좌표를 입력하세요.=>"))

if x > 0 and y > 0:
    print(f"입력한 좌표는 1사분면입니다.")
elif x > 0 and y < 0:
    print(f"입력한 좌표는 4사분면입니다.")
elif x < 0  and y > 0:
    print(f"입력한 좌표는 2사분면입니다.")
elif x < 0 and  y < 0:
    print(f"입력한 좌표는 3사분면입니다.")
else:
    if x == 0  and y != 0:
        print(f"입력한 좌표는 y축 위에 있습니다.")
    elif x != 0  and y == 0:
        print(f"입력한 좌표는 x축 위에 있습니다.")
    else:
        print(f"입력한 좌표는 원점에 있습니다.")