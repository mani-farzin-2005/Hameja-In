from django.core.paginator import Paginator
from django.shortcuts import render , get_object_or_404
from .models import *
from blog.models import *
from tour.models import TourGroup, Tour, Tagss
from django.db.models import Q

def home(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac=ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    recent_tours=Tour.objects.all().order_by('-last_update')[:8]

    tagg = Tagss.objects.get(name='kish')
    kish = Tour.objects.filter(tags=tagg).order_by('-last_update')[:8]

    print(web.logo.url)

    if request.method=='GET':
        search = request.GET.get('s','').strip()
        if search:
            posts = Post.objects.filter(
                Q(title__icontains=search)|Q(author__person__username__icontains=search)|Q(tags__name__icontains=search)
            ).order_by('-published_date')
            heads = HeaderObject.objects.filter(is_childern=False)
            web = WebInfo.objects.get()
            contac = ContactUs.objects.get()
            abo = AboutUs.objects.get()
            bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
            blog_count = Post.objects.filter(status=True).count()
            paginator = Paginator(posts, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            tags = Tags.objects.all()

            return render(request, 'blog-home.html',
                          {'posts': page_obj, 'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo,
                           'blogs': bl,
                           'blog_count': blog_count,'tags':tags})

    return render(request,'index.html',{'headers':heads,'website':web,'contact_us':contac,'about_us':abo,'blogs':bl,'recent_tours':recent_tours,'kish_tours':kish})

def test(request):
    return render(request,'404.html')
def p404(reqeust , exception):
    return render(reqeust,'404.html' , status=404)
def contact(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]

    return render(request,'contact-us.html',{'headers':heads,'website':web,'contact_us':contac,'about_us':abo,'blogs':bl})
def about(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]

    return render(request ,'about-us.html',{'headers':heads,'website':web,'contact_us':contac,'about_us':abo,'blogs':bl})
def all_tour(request , id):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]

    tourr = get_object_or_404(TourGroup,id = id)
    return render(request, 'tour-home.html', {'tour':tourr,'headers':heads,'website':web,'contact_us':contac,'about_us':abo,'blogs':bl})
def tag(request,tag_name):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    blog_count =Post.objects.filter(status=True).count()
    tagg = get_object_or_404(Tags,id=tag_name)
    posts = Post.objects.filter(tags=tagg).order_by('-published_date')
    tags = Tags.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog-home.html' , {'posts':page_obj,'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl , 'blog_count':blog_count,'tags':tags})


def post(request,id):
    possst = get_object_or_404(Post,id=id)
    possst.views+=1
    possst.save()
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    tags = Tags.objects.all()
    blog_count = Post.objects.filter(status=True).count()
    if request.method=='POST':
        name = request.POST.get('author')
        email = request.POST.get('email')
        websit = request.POST.get('name')
        comment = request.POST.get('comment')
        refering_comment = request.POST.get('refering-comment')
        if refering_comment==None:
            x = Comment.objects.create(name=name,email=email,website=websit,text=comment ,post_id=id)
            x.save()
        else:
            x = Comment.objects.create(name=name, email=email, website=websit, text=comment, post_id=id,reply_id=refering_comment)
            x.save()

    comments =Comment.objects.filter(post=possst,is_reply=False,display=True)
    for com in comments:
        print(com.name)
    return render(request, 'blog-single.html', {"post": possst,'comments':comments, 'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl,'tags':tags, 'blog_count':blog_count})