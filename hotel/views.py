from django.core.paginator import Paginator

from blog.models import Post, Tags
from website.models import *
from .models import *
from django.shortcuts import *
def test(request):
    return render(request,'test.html')
def home(request):
    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    hotels = Hotel.objects.all().order_by('rating')
    paginator = Paginator(hotels, 6)
    tags = Tags.objects.all()
    post_number =Post.objects.count()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'hotel-home.html' , {'tags':tags,'post_number':post_number,  'hotels':page_obj,'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl})
def single(request , id):


    heads = HeaderObject.objects.filter(is_childern=False)
    web = WebInfo.objects.get()
    contac = ContactUs.objects.get()
    abo = AboutUs.objects.get()
    bl = Post.objects.filter(status=True).order_by('-published_date')[:3]
    hot = Hotel.objects.get(id=id)
    service = Service_Hotel.objects.filter(tour=hot)
    if request.method=='POST':
        name = request.POST.get('author')
        email = request.POST.get('email')
        websit = request.POST.get('name')
        comment = request.POST.get('comment')
        refering_comment = request.POST.get('refering-comment')
        if refering_comment == None:
            x = Comment.objects.create(name=name, email=email, website=websit, text=comment, hotel_id=id)
            x.save()
        else:
            x = Comment.objects.create(name=name, email=email, website=websit, text=comment, hotel_id=id,
                                       reply_id=refering_comment)
            x.save()
    comments = Comment.objects.filter(is_reply=False,hotel=hot,display=True)
    return render(request,'hotel-single.html',{'hotel':hot,'headers': heads, 'website': web, 'contact_us': contac, 'about_us': abo, 'blogs': bl , 'services':service,'comments':comments })