import time

def count_down(count):
    for n in range(count):
        print( f"{count - n}...", end="\r")
        time.sleep(1)
    print("Bomb!!")
    
def main():
    count_down(10)
        




if __name__ == "__main__":
    main()