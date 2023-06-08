from django.contrib import admin
from .models import YouTubeVideo
# Register your models here.

class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'channel')


admin.site.register(YouTubeVideo, YouTubeVideoAdmin)