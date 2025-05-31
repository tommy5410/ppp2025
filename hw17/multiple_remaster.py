import random
import tkinter as tk
from tkinter import simpledialog
import rich

# tkinter 창 숨기기
window = tk.Tk()
window.withdraw()

# GUI 입력 함수
def gui_input(text):
    return simpledialog.askstring(title="구구단 문제", prompt=text)

def problem():
    dan = random.randint(1, 9)
    mul = random.randint(1, 9)

    ans_str = gui_input(f"{dan} X {mul} = ?")
    if ans_str is None:
        return False

    if not ans_str.isdigit():
        return False

    ans = int(ans_str)

    if ans == dan * mul:
        rich.print("[green]정답![/green]")
        return True
    else:
        rich.print("[red]오답![/red]")
        return False

def main():
    score = 0
    total_problem = 5
    for n in range(total_problem):
        is_correct = problem()
        if is_correct:
            score += 1
    rich.print(f"총점은 [bold cyan]{score}[/bold cyan], [bold magenta]{score / total_problem * 100}점[/bold magenta]")

if __name__ == "__main__":
    main()