#영단어 글자수

text = input("문자를 입력하시오.: ")
print(text)    # text값을 출력시켜주는식
print(len(text))  #몇글자인지 함수
print("=" * 30)   
print(text.upper()) #대문자로 바꿔주기 함수
print(text.lower()) #소문자로 바꿔주기 함수
print("===========================")  # 없어도됨 
print(text[:5]) # 앞에 3글자 
print(text[-2:]) #뒤에서 2글자 

text = ['a','b','c','d','e','f','g','h'] #리스트 사용법
text = "abcdefgh"
print(text[2:6])