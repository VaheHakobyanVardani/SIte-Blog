from django import  template

from blog.models import Category, Post

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories':categories, 'menu_class':menu_class}

@register.inclusion_tag('blog/sidebar_menu.html')
def show_menu_sidebar(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories':categories, 'menu_class':menu_class}

@register.inclusion_tag('blog/recent_posts.html')
def get_recent_posts(cnt=4):
    posts = Post.objects.order_by('-created_at')[:cnt]
    return {'posts': posts}
