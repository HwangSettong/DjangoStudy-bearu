"""
class 클래스():
    # 초기값 설정
    # def __init__(self):
    #     self.변수 = 1
    변수 = 1
    
    def 변수변경(self):  # self를 이용해서 객체의 변수를 사용할 수 있다.
        self.변수 = 3
"""

"""
!! 모든 사원들은 각자
출근하시면
아침업무로
배달온 상자안에 물건을 전부 까서
사과는 냉장실에
아이스크림은 냉동실에 넣어주시고
나머지는 폐기처분 해주세요.
!! 그리고 아침업무 체크를 해주세요.
"""
class 업무():
    아침업무유무 = False
    def 아침업무체크(self):
        self.아침업무유무 = True

    def 아침업무(self, 상자):
        for 물건 in 상자:
            if 물건 == "사과":
                print(f"'{물건}'은 냉장고에 넣습니다.")
            elif 물건 == "아이스크림":
                print(f"'{물건}'은 냉동실에 넣습니다.")
            else:
                print(f"'{물건}'은 폐기처분 합니다.")
        self.아침업무체크()


출근 = True
if 출근:
    상자 = ["콩", "콩", "콩", "사과"]
    Tommy_업무 = 업무()
    print(Tommy_업무.아침업무유무)
    Tommy_업무.아침업무(상자)
    print(Tommy_업무.아침업무유무)
    
    Sera_업무 = 업무()
    print(Sera_업무.아침업무유무)
