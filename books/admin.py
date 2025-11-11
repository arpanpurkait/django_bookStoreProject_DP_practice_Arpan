from django.contrib import admin

# Register your models here.

from .models import Book
class BookkAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    #search_fileds = ('title', 'author')




admin.site.register(Book)