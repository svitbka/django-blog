from blog.models import Post, Tag
from django import template

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def show_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog/tags_tpl.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
