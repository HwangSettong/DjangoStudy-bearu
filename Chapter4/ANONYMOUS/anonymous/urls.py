from django.urls import path
from board.views import board # import function 'board' of 'board/views'
from user.views import signin # import function 'signin' of 'user/views'
from user.views import signup # import function 'signup' of 'user/views'
urlpatterns = [
    # path(경로, 함수) : 해당 경로로 요청이 들어오면 함수 실행한다.
    path('', board, name="board"),
    path('user/signin', signin, name="signin"),
    path('user/signup', signup, name="signup"),
]
