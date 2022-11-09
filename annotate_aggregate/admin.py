from django.contrib import admin

from .models import Author, Publisher, Book, Store


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "pages", "price", "rating", "pubdate",)
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]
    list_display_links = ('name', 'pages',)
    list_filter = ['name', 'price']
    search_fields = ['name']
    date_hierarchy = 'timestamp'
    list_per_page = 10
    save_as = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "age",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)
