from django.shortcuts import render, redirect
from board.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required # login_required라는 decorator를 가져옴
from django.core.files.storage import default_storage # 장고에서 내부적으로 파일시스템을 관장할 때 해당 파일을 변경/저장/삭제 하는 함수
import uuid

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

@login_required(login_url="signin")
def post_write(request):
    if request.method == "GET":
        return render(request, 'page/post_write.html')
    
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        img = request.FILES.get("img",None) # request.FILES["img"] 로 받으면 이미지파일을 필수로 받아야함.
        if img:
            img_name = uuid.uuid4 # 랜덤으로 고유의 값을 반환함.
            ext = img.name.split('.')[-1] # 파일 이름에서 확장자만 가져옴.
            img_url = f"{img_name}.{ext}"
            default_storage.save(img_url, img) # default_storage.save("경로", img)
        else:
            img_url = ""
        Post(
            user = request.user,
            title = title,
            content = content,
            img_url = img_url,
        ).save()
        return redirect('board')

