from django.contrib import admin

from .models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated']
    search_fields = ['title']


admin.site.register(Story, StoryAdmin)