from django.shortcuts import render, get_object_or_404

from blog.models import Post, Tags ,Comment
from website.models import HeaderObject, WebInfo, ContactUs, AboutUs
from django.core.paginator import Paginator

def test(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    blog_count = Post.objects.filter(status=True).count()
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 6)
    tags = Tags.objects.all()

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog-home.html',
                  {'posts': page_obj, 'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl,
                   'blog_count': blog_count , 'tags':tags})