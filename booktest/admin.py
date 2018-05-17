from django.contrib import admin

# Register your models here.

from models import BookInfo,HeroInfo


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 5


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['id']
    list_per_page = 1
    # fields = ['bpub_date','btitle']
    fieldsets =[
        ('basic',{'fields':['btitle']}),
        ('more',{'fields':['bpub_date']}),
    ]
    inlines = [HeroInfoInline]



admin.site.register(BookInfo,BookInfoAdmin)
