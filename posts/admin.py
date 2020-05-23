from django.contrib import admin
from .models import Feed

# Register your models here.


class FeedAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Feed, FeedAdmin)
