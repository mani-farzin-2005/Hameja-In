
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .utils import get_named_url_choices
from django.contrib import admin
from .models import WebInfo, AboutUs, ContactUs, HeaderObject , Advertising
from solo.admin import SingletonModelAdmin


class HeaderObjectForm(forms.ModelForm):
    href = forms.ChoiceField(choices=get_named_url_choices)

    class Meta:
        model = HeaderObject
        fields = '__all__'


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = WebInfo
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }
@admin.register(WebInfo)
class WebInfoAdmin(SingletonModelAdmin):

    list_display = ('description', 'logo', 'copy_right')

@admin.register(Advertising)
class advertising(admin.ModelAdmin):
    list_display = ('video_file','content')

@admin.register(AboutUs)
class AboutUsAdmin(SingletonModelAdmin):
    form = PostAdminForm
    list_display = ('about_us_small',)


@admin.register(ContactUs)
class ContactUsAdmin(SingletonModelAdmin):
    list_display = ('phone_number', 'email', 'address')


@admin.register(HeaderObject)
class HeaderObjectAdmin(admin.ModelAdmin):
    form = HeaderObjectForm

    list_display = ('name', 'href', 'parent' )
    fields = ('name', 'href', 'parent' , 'is_childern' )

    def parent_name(self, obj):
        return obj.parent.name if obj.parent else '-'
    parent_name.short_description = "Parent"
