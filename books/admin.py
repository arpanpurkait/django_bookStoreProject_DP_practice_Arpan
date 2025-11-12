from django.contrib import admin
from .models import Review
# Register your models here.


from .models import Book
class ReviewInline(admin.TabularInline):
    model = Review




class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    inlines = [ReviewInline] 




admin.site.register(Book,BookAdmin)