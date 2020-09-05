from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import PostForm
from .models import Tag
from .models import Post
# Create your views here.

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, "포스팅을 저장했습니다.")
            #return redirect("/") # TODO: get_absolute_url활용
            #model.get_absolute_url() 을 만들면 redirect의 인자로 model instance를 넣을 수 있는듯?
            return redirect(post) 
            
    else:
        form = PostForm()
    return render(request, "instagram/post_form.html", {
        "form":form, 
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "instagram/post_detail.html", {
        "post":post,
    })

def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    return render(request, "instagram/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
    })


