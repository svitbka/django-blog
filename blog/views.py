from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Category, Tag, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, ListView
from django.db.models import F 


def index(request):
    title = "Blog"
    posts = Post.objects.all()
    

    return render(request, template_name='blog/index.html', context={'title': title, 'posts': posts})


def get_category(request, slug):
    contact_list = Post.objects.filter(category__slug=slug)
    paginator = Paginator(contact_list, 4)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
 
    title = "Category"
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'page_obj': page_obj, 'title': title, 'posts': posts})


def get_tag(request, slug):
    contact_list = Post.objects.filter(tags__slug=slug)
    paginator = Paginator(contact_list, 4)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
 
    title = "Category"
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'page_obj': page_obj, 'title': title, 'posts': posts})



class PostDetailView(DetailView):
    model = Post  
    template_name = "blog/single.html"
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    template_name = "blog/search.html"
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context