import random

CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

def get_chosung(word):
    result = ""
    for ch in word:
        if ord('가') <= ord(ch) <= ord('힣'):
            code = ord(ch) - ord('가')
            chosung_index = code // 588
            result += CHOSUNG_LIST[chosung_index]
        else:
            result += ch
    return result

def main():
    words = ["바나나", "딸기", "토마토", "복숭아"]
    answer = random.choice(words)
    print(get_chosung(answer))
    for _ in range(3):
        user_input = input()
        if user_input == answer:
            print("정답입니다")
            return
        else:
            print("오답입니다.")
    print("게임오버")

if __name__ == "__main__":
    main()