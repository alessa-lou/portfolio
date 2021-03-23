from django.contrib import admin
from blog.models import Post, Category
#above line: models you want to register on admin page

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# last two lines register models with the admin classes

