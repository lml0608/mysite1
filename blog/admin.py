from django.contrib import admin

from .models import Author,Book,Publish

# Register your models here.


#创建并制定ModelAdmin对象

#方法一

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):

    #列表展示
    list_display = ('id','name','price','pub_date')
    #列表修改字段
    list_editable = ('name','price')

    #过滤
    list_filter = ('pub_date',)

    date_hierarchy = "pub_date"

    #列表排序
    ordering = ('-pub_date',)
    #字段展示顺序
    fields = ('name','price','pub_date','publish','author')
    #改变多对多关系的选择方式，横向
    filter_horizontal = ('author',)
    #模糊搜索
    search_fields = ('id','name','price')
    #每页展示条目数
    list_per_page = 3

class PublishAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(Book,BookAdmin)

#方法二 使用装饰器
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     pass
