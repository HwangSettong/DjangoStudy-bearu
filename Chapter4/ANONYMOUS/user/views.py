from django.contrib import messages
from django.shortcuts import render, redirect
# render(request, template_name, context=None, content_type=None, status=None, using=None) : HttpResponse렌더링된 텍스트가 포함된 객체를 반환
# redirect(to, *args, permanent=False, **kwargs) : HttpResponseRedirect전달된 인수에 대한 적절한 URL을 반환
from django.contrib.auth import authenticate, login
# authenticate(request=None, **credentials): User 인증 함수. 자격 증명이 유효한 경우 User 객체를, 그렇지 않은 경우 None을 반환
# login(request, user, backend=None) : 로그인 함수. Django의 세션 프레임 워크를 사용하여 세션에 인증된 사용자의 ID를 저장
from django.contrib.auth.hashers import make_password
# make_password(password, salt=None, hasher='default') : 해시된 비밀번호를 생성
from user.models import User # import class 'User' of 'user/models.py'


def signin(request):
    if request.method == "GET":
        return render(request, 'page/signin.html')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password) # authenticate함수로 유효한 유저인지 확인

        if user:                        # 사용자 인증이 되어 user객체를 반환하면
            login(request, user)        # login 세션에 사용자 저장하고
            return redirect('board')    # 게시판 페이지로 redirect
        else:                                                   # 사용자 인증에 실패하여 None을 반환하면
            messages.error(request, "아이디, 비밀번호를 확인해주세요")  # 에러메세지 전달하고
            return redirect('signin')                           # 다시 로그인 페이지로 다시 redirect


def signup(request):
    if request.method == "GET":
        return render(request, 'page/signup.html')
    if request.method == "POST":
        username = request.POST["username"]
        password = make_password(request.POST["password"]) # 비밀번호 해시화
        nickname = request.POST["nickname"]

        user = User.objects.filter(username=username)
        # exists : 존재하면 True, 존재하지 않으면 False
        if user.exists():
            messages.error(request, "이미 가입한 아이디 입니다.")
            print("dddd")
            return redirect('signin')
        else:
            print("aaaa")
            new_user = User(
                username = username,
                password = password,
                nickname = nickname,
            )
            new_user.save() # data insert
            login(request, new_user) # login 세션에 사용자 바로 저장
            return redirect("board")