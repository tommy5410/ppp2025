import time
import tkinter as tk
from tkinter import simpledialog
import rich

# 창 숨기기
window = tk.Tk()
window.withdraw()

# GUI 입력 함수
def gui_input(text):
    return simpledialog.askstring(title=" 입력창 ", prompt=text)

# 카운트다운 함수 (수업시간 방식 유지)
def count_down_timer(seconds):
    for n in range(seconds):
        print(f"{seconds - n}...", end="\r")
        time.sleep(1)
    rich.print("[bold red]💣 Boom!! 💣[/bold red]")

# 메인 함수 (아주 간단하게)
def main():
    sec = gui_input("몇 초로 설정할까요?")
    
    if sec != None:
        if sec.isdigit():
            count_down_timer(int(sec))

if __name__ == "__main__":
    main()