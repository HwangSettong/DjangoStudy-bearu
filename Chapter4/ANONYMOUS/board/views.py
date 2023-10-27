from django.shortcuts import render
from board.models import Post
from django.core.paginator import Paginator

def board(request):
    if request.method == "GET":
        page = request.GET.get('page', 1) # page 파라미터를 받으며 default 값은 1
        search_text = request.GET.get('search_text', "") # search_text 파라미터를 받으며 default 값은 ""
        post_set = Post.objects.filter(
                        title__icontains=search_text # title 컬럼에서 대소문자 상관없이 search_text가 포함되어 있는 데이터들 
                    ).all().order_by('-id')
        paginator = Paginator(post_set, 4)

        post_set = paginator.get_page(page)
        
        context ={
            'post_set' : post_set,
            'search_text' : search_text,

        }
        
        return render(request, 'page/index.html', context= context)

def post_write(request):
    if request.method == "GET":
        return render(request, 'page/post_write.html')

