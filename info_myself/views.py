from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post_i
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post_i.objects
    return render(request, 'info_myself/home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post_i, pk = post_id)
    return render(request, 'info_myself/detail.html', {'post':post_detail})

def post_new(request):
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm()
        return render(request, 'info_myself/new.html', {'form':form})