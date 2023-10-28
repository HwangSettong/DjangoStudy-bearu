from django.urls import path
from board.views import board, post_write, post_detail # import function 'board', 'post_write', 'post_detail' of 'board/views'
from user.views import signin, signup, signout # import function 'signin','signup', 'signout' of 'user/views'
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path(경로, 함수) : 해당 경로로 요청이 들어오면 함수 실행한다.
    path('', board, name="board"),
    path('user/signin', signin, name="signin"),
    path('user/signup', signup, name="signup"),
    path('user/signout', signout, name="signout"),

    path('post/write', post_write, name="post_write"),
    path('post/<int:post_id>', post_detail, name="post_detail"),
]

if settings.DEBUG:
# settings.DEBUG가 True이면(개발중이라면)
    urlpatterns += static('upload', document_root=settings.MEDIA_ROOT) 
    # upload라는 경로로 들어와서 정적인 파일들을 매칭해서 보여줘라. 정적인 파일들을 settings.py에 MEDEIA_ROOT로 지정 해두었다.
