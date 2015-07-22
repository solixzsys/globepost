from django.contrib import admin
from newsapp.models import Website, Country, Channel,Post
#, Post


class WebsiteAdmin(admin.ModelAdmin):
    list_display=('id','site_name','site_url','category','country')

class CountryAdmin(admin.ModelAdmin):
    list_display=('id','country_name','country_code')

class ChannelAdmin(admin.ModelAdmin):
    list_display=('id','channel_title','feed_url','site','category','country')

class PostAdmin(admin.ModelAdmin):
    list_display=('id','site','feed_url','title','pub_date','summary','content','thumbnail','post_url')
    date_hierarchy = 'pub_date'
    ordering=['-pub_date']
    search_fields=['title']
admin.site.register(Website,WebsiteAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Channel,ChannelAdmin)

admin.site.register(Post,PostAdmin)