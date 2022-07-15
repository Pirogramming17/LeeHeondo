from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    return render(request, 'posting/post_list.html', {})

def post_list(request):
    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at') # posts : 쿼리셋의 이름
    return render(request, 'posting/post_list.html', {'posts': posts})

    # 게시일 기준으로 정렬
    #request: 사용자가 요청하는 모든 정보
    # {'posts': posts} -> 템플릿을 사용하기 위한 매개변수? 'posts'라는 이름으로 쿼리셋 posts를 전달