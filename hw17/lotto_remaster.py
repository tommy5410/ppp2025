import random
import rich

def get_lotto():
    lotto_list = []
    while True:
        n = random.randint(1,45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list) == 6:
            break
    return sorted(lotto_list)

def main():
    lotto_num = get_lotto()
    rich.print(f"[bold blue]이번 주 로또 번호:[/bold blue] [yellow]{lotto_num}[/yellow]")

if __name__ == "__main__":
    main()