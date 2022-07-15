from django.shortcuts import render, get_object_or_404, redirect 
from django.utils import timezone
from .models import Post
from .forms import PostForm


# 게시일 기준으로 정렬
#request: 사용자가 요청하는 모든 정보
# {'posts': posts} -> 템플릿을 사용하기 위한 매개변수? 'posts'라는 이름으로 쿼리셋 posts를 전달

def post_list(request):
    return render(request, 'posting/post_list.html', {})

def post_list(request):
    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at') # posts : 쿼리셋의 이름
    return render(request, 'posting/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # pk(게시글의 고유한 값)에 해당하는 Post가 없을 경우 또는 가져오기
    return render(request, 'posting/post_detail.html', {'post': post}) 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posting/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # 수정하고자 하는 게시글의 모델로 가져온다
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) #모델 인스턴스로 넘겨주기
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.updated_at= timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posting/post_edit.html', {'form': form})