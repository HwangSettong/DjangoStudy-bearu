"""
if 조건:
    코드
elif 조건:
    코드
else:
    코드
"""
# 비교 연산자나 조건 연산자와 함께 많이 쓰임
"""
!! 비교연산자
값 == 값 : 양쪽의 값이 서로 같다
값 != 값 : 양쪽의 값이 서로 다르다
값 > 값, 값 < 값, 값 >= 값, 값 <= 값 : 양쪽 값 크기 비교

!! 조건연산자
1조건 and 2조건 : 1조건이 만족하면서 2조건 만족
1조건 or 2조건 : 1조건 2조건 중 하나만 만족해도 만족
"""

a = 3
b = 5
print(a == b) # False
print(a == 3 and b != 5) # False
print(a == 3 or b != 5)  # True

"""
숙제1.
사과는 냉장실에
아이스크림은 냉동실에 넣어주시고
나머지는 폐기처분 해주세요.
"""
변수 = "사과"
if 변수 == "사과":
    print("냉장실")
elif 변수 == "아이스크림":
    print("냉동실")
else:
    print("폐기")