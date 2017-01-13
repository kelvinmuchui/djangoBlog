from django.contrib import admin

from .models import Posts

#making the modelvisible on the admin page

admin.site.register(Posts)
