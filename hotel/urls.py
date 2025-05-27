from django.urls import path
from . import views
app_name = 'hotels'
urlpatterns =[
    path('' ,views.home,name = 'home'),
    path('ht/<int:id>' ,views.single,name = 'single'),
]