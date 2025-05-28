from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render , get_object_or_404
from jalali_date import datetime2jalali

from website.models import *
from blog.models import Post, Tags
from .models import *
import random
from moviepy import VideoFileClip
import datetime
import mimetypes
def get_mime_type(file_path):
    import mimetypes
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type

def format_duration(seconds):
    import datetime
    return str(datetime.timedelta(seconds=int(seconds)))

def get_video_duration(path):
    from moviepy import VideoFileClip
    clip = VideoFileClip(path)
    duration = clip.duration  # in seconds
    clip.close()
    return duration
def all_tour(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    suggestions = Suggestion_pack.objects.all()
    x =[]
    for suggest in suggestions:
        for tour in suggest.tours.all:
            x.append(tour)
    return render(request,'tour-suggestion.html',{'alltour':x,'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl,'suggestions':suggestions})

def Package(request, id):
    from django.shortcuts import render, get_object_or_404
    import random

    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    tour = get_object_or_404(TourGroup, id=id)
    sametour = TourGroup.objects.filter(tags__in=tour.tags.all()).exclude(id=tour.id).distinct()
    count = Advertising.objects.count()
    random_obj = Advertising.objects.all()[random.randint(0, count - 1)]
    vid_path = random_obj.video_file.path
    vid_duration = format_duration(get_video_duration(vid_path))
    typp = get_mime_type(vid_path)
    print(typp)
    return render(request, 'tour_group.html', {
        'package': tour,
        'headers': heads,
        'website': web,
        'contact_us': contac,
        'about_us': abo,
        'blogs': bl,
        'samepackages': sametour,
        'ads': random_obj,
        'video_timer': vid_duration,
        'ty': typp
    })

def home(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    blog_count = Post.objects.filter(status=True).count()
    t = Tags.objects.all()
    ta = Tagss.objects.all()
    to = Tour.objects.all().order_by('-last_update')
    paginator = Paginator(to, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'tour-home.html' ,{'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl,'post_numbers':blog_count,'post_tags':t,'tags':ta , 'tours':page_obj})

def tag(request , name):

    tag =Tagss.objects.get(id = name)
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    blog_count = Post.objects.filter(status=True).count()
    t = Tags.objects.all()
    ta = Tagss.objects.all()
    to = Tour.objects.filter(tags = tag).order_by('-last_update')
    paginator = Paginator(to, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tour-home.html',
                  {'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl,
                   'post_numbers': blog_count, 'post_tags': t, 'tags': ta, 'tours': page_obj})

def single(request , id):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    tour = get_object_or_404(Tour, id=id)
    sametour = Tour.objects.filter(tags__in=tour.tags.all()).exclude(id=tour.id).distinct()
    ta = Tagss.objects.all()
    comments = Comment.objects.filter(tour=tour,display=True,is_reply=False)
    print(comments.count())
    if request.method=='POST':
        name = request.POST.get('author')
        email = request.POST.get('email')
        websit = request.POST.get('name')
        comment = request.POST.get('comment')
        refering_comment = request.POST.get('refering-comment')
        if refering_comment==None:
            x = Comment.objects.create(name=name,email=email,website=websit,text=comment ,tour_id=id)
            x.save()
            return JsonResponse({
                "id":x.id,
                "name": x.name,
                "email": x.email,
                "website": x.website,
                "comment": x.text,
                "time": datetime2jalali(x.time).strftime('%Y/%m/%d')
            })
        else:
            x = Comment.objects.create(name=name, email=email, website=websit, text=comment, tour_id=id,reply_id=refering_comment)
            x.save()
            return JsonResponse({
                "id":x.id,
                "name": x.name,
                "email": x.email,
                "website": x.website,
                "comment": x.text,
                "time": datetime2jalali(x.time).strftime('%Y/%m/%d'),
                "refer":x.reply_id
            })
    return render(request, 'tour-single.html', {'tour':tour,'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl,'sametour':sametour,'tour_tags':ta , 'comments':comments})