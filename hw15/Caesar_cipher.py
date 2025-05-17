def caesar_encode(text, shift=3):
    result = ""
    for ch in text:
        code = ord(ch)
        if 97 <= code <= 122:
            code = code + shift
            if code > 122:
                code = 97 + (code - 123)
            result += chr(code)
        elif 65 <= code <= 90:
            code = code + shift
            if code > 90:
                code = 65 + (code - 91)
            result += chr(code)
        else:
            result += ch
    return result

def caesar_decode(text, shift=3):
    result = ""
    for ch in text:
        code = ord(ch)
        if 97 <= code <= 122:
            code = code - shift
            if code < 97:
                code = 122 - (96 - code)
            result += chr(code)
        elif 65 <= code <= 90:
            code = code - shift
            if code < 65:
                code = 90 - (64 - code)
            result += chr(code)
        else:
            result += ch
    return result

def main():
    plain_text = input("문장 입력: ")
    encoded_text = caesar_encode(plain_text)
    print(encoded_text)
    decoded_text = caesar_decode(encoded_text)
    print(decoded_text)

if __name__ == "__main__":
    main()