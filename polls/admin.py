from django.contrib import admin

from polls.models import Choice, Poll, Article

# Register your models here.


admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Article)