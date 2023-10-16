from django.urls import path
from board.views import board # import function 'board' of 'board/views'

urlpatterns = [
    # path(경로, 함수) : 해당 경로로 요청이 들어오면 함수 실행한다.
    path('', board, name="board"),
]

