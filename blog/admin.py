from django.contrib import admin
from blog.models import *

# Register your models here

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title','desc',)
    list_editable = ('click_count',)

    fieldsets = (
        (None,{
            'fields':('title','desc','content','tag','user','category')
        }),
        ('高级设置',{
            'classes':('collapse',),
            'fields':('click_count','is_recommend',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.1/kindeditor-min.js',
            '/static/js/kindeditor-4.1.1/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.1/config.js',
        )

class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'article', 'content',)

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
# admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad)
