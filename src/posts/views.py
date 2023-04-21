from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, PostView, Like, Comment
from .forms import PostForm

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url= '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url= '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class PostDeteleView(DeleteView):
    model = Post
    success_url= '/'


"""
def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_query_set = Like.objects.filter(user=request.user, post=post)
    if like_query_set.exists():
        like_query_set[0].delete()
        return redirect('post_like.html', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('post_like.html', slug=slug)
"""