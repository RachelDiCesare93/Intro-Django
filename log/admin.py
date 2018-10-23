from django.contrib import admin

from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Topic, TopicAdmin)
