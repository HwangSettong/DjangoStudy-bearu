from django.shortcuts import render
from board.models import Post

def board(request):
    if request.method == "GET":
        post_set = Post.objects.all()
        
        context ={
            'post_set' : post_set

        }
        return render(request, 'page/index.html', context= context)

