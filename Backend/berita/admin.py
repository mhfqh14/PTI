from django.contrib import admin

# Register your models here.
from .models import berita

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ['slug',]

admin.site.register(berita, PostAdmin)
