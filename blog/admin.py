from django.contrib import admin
from .models import Author, Tags, Post , Comment
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date import datetime2jalali
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from django.utils.translation import gettext_lazy as _


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'person')
    search_fields = ('person__username', 'person__email')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'email' , 'website')
    fields = ('name' , 'email' , 'website' , 'text', 'post' , 'display','reply','is_reply')


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_date'] = SplitJalaliDateTimeField(label=_('created date'), widget=AdminSplitJalaliDateTime)

        self.fields['published_date'] = SplitJalaliDateTimeField(label=_('published date'), widget= AdminSplitJalaliDateTime)



@admin.register(Post)
class PostAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    form = PostAdminForm  # or TestForm if you use that with Jalali widgets
    list_display = ('id', 'title', 'author', 'created_date', 'published_date','status', 'views', 'video_file'  )
    list_filter = ('status', 'published_date', 'tags')
    search_fields = ('title', 'description', 'author__person__username')
    filter_horizontal = ('tags',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

    fields = (
        'title', 'description', 'video_file','link_to_other_site', 'content', 'views', 'tags', 'image',
        'author', 'created_date','published_date', 'status' , 'instagram' , 'linkdin' , 'twitter' , 'facebook','comments'
    )

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')

