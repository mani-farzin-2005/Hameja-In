

# Register your models here.
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget

from hotel.models import Hotel , Service_Hotel
from .models import TourGroup, Document, Flight, Tour, Comment, Service,Tagss,Suggestion_pack
from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _


class BookInlin(admin.TabularInline):  # Or use `StackedInline` for a different layout
    model = Service_Hotel  # Link the Book model
    fields = ['name']  # Fields to display
    extra = 0


class BookInline(admin.TabularInline):  # Or use `StackedInline` for a different layout
    model = Service  # Link the Book model
    fields = ['name']  # Fields to display
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'email' , 'website')
    fields = ('name' , 'email' , 'website' , 'text', 'tour' , 'display')

class TourGroupForm(forms.ModelForm):
    class Meta:
        model = TourGroup
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }

@admin.register(TourGroup)
class TourGroupAdmin(admin.ModelAdmin):
    form = TourGroupForm
    list_display = ('id', 'title' )
    filter_horizontal = ['tags']
    search_fields = ('title',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
@admin.register(Tagss)
class Tga(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Suggestion_pack)
class suggest(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ['tours']


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    form = PostAdminForm
    fields = ('name','content','description','city','price','rating','main_image','service','address','email','website','phone_number','latitude','longitude', 'comments','picture1','picture2','picture3','picture4','picture5','picture6','picture7','breakfast')
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [BookInlin]


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['beginning_time'] = SplitJalaliDateTimeField(label=_('beginning time'), widget= AdminSplitJalaliDateTime)

        self.fields['end_time'] = SplitJalaliDateTimeField(label=_('end time'), widget= AdminSplitJalaliDateTime)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'start_hour', 'reach_hour')


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'] = JalaliDateField(label=_('start date'), widget=AdminJalaliDateWidget)

        self.fields['return_date'] = JalaliDateField(label=_('return date'), widget=AdminJalaliDateWidget)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    form = TourForm
    inlines = [BookInline]
    list_display = ('id', 'name', 'tour_group', 'origin', 'destination', 'duration', 'price', 'start_date', 'return_date' ,'last_update')
    list_filter = ('origin', 'destination', 'start_date')
    search_fields = ('name', 'origin', 'destination')
    filter_horizontal = ('document', 'hotell','tags' )
    readonly_fields = ('last_update',)
