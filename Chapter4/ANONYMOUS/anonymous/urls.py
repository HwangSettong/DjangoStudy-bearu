from django.urls import path
from board.views import board, post_write # import function 'board', 'post_write' of 'board/views'
from user.views import signin, signup, signout # import function 'signin','signup', 'signout' of 'user/views'

urlpatterns = [
    # path(경로, 함수) : 해당 경로로 요청이 들어오면 함수 실행한다.
    path('', board, name="board"),
    path('user/signin', signin, name="signin"),
    path('user/signup', signup, name="signup"),
    path('user/signout', signout, name="signout"),
    path('post/write', post_write, name="post_write"),
]
