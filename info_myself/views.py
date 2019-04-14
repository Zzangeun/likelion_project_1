from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post_i
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post_i.objects
    return render(request, 'info_myself/home.html', {'posts':posts})

def my_infomation(request, post_id):
    post_my_infomation = get_object_or_404(Post_i, pk = post_id)
    return render(request, 'info_myself/my_infomation.html', {'post':post_my_infomation})