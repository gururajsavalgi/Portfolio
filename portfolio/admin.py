from django.contrib import admin

# Register your models here.
from .models import Index, Contact,Projects,Skills,People

admin.site.register(Contact)
admin.site.register(Index)
admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(People)