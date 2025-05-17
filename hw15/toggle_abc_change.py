def toggle_text(text: str) -> str:
    txt_list = []
    for ch in text:
        if 'a' <= ch <= 'z':
            txt_list.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z':
            txt_list.append(chr(ord(ch) + 32))
        else:
            txt_list.append(ch)
    return "".join(txt_list)

def main():
    print(toggle_text(input("문자열을 입력하세요: ")))

if __name__ == "__main__":
    main()
    