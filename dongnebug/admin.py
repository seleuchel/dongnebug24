from django.contrib import admin
from dongnebug.models import Complain, Favorite, Comment, Sympathy

admin.site.register(Complain)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Sympathy)