import random
import tkinter as tk
from tkinter import simpledialog
import rich

# tkinter 창 숨기기
window = tk.Tk()
window.withdraw()

# 입력 함수
def gui_input(text):
    return simpledialog.askstring(title="행맨 게임", prompt=text)

# 행맨 로직
def hangman(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True
    return is_correct

# 메인 함수
def main():
    problem = ["cafe", "baseball", "festival"]
    solution = problem[random.randrange(len(problem))]
    lives = 5
    answer = ["_" for n in range(len(solution)) ]
    
    print(answer)

    while True:
        input_ch = gui_input(f"{''.join(answer)}? => _ 안에 무슨 글자가 들어갈까요?")
        
        if input_ch == None:
            continue  # 사용자가 취소 눌렀을 때 무시

        if hangman(solution, answer, input_ch):
            rich.print(f"[green]{input_ch}가 들어있습니다.[/green]")
        else:
            lives -= 1

        if lives <= 0:
            rich.print(f"[red]기회 소진되었습니다. 정답은 {solution} 였습니다.[/red]")
            break

        if "_" not in answer:
            rich.print(f"[bold blue]정답은 {solution}! 잘하셨습니다. 게임 종료[/bold blue]")
            break

        elif input_ch not in solution:
            print("오답입니다. 다시 해보세요.")

if __name__ == "__main__":
    main()