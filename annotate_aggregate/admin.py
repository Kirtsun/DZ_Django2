from django.contrib import admin

from .models import Author, Publisher, Book, Store


class BookInLineAuthor(admin.TabularInline):
    model = Book.authors.through
    extra = 3


class BookInLine(admin.TabularInline):
    model = Book
    extra = 3


class BookInLineStore(admin.TabularInline):
    model = Store.books.through
    extra = 3


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [BookInLine]
    list_display_links = ('name', )
    list_filter = ['name']
    search_fields = ['name']
    save_as = True


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "pages", "price", "rating", "pubdate",)
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Info', {'fields': ['pages', 'price', 'rating', 'pubdate']}),
    ]
    list_display_links = ('name', 'pages',)
    list_filter = ['rating', 'price']
    search_fields = ['name']
    date_hierarchy = 'pubdate'
    list_per_page = 20
    save_as = True
    inlines = [BookInLineStore, BookInLineAuthor]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "age",)
    list_display_links = ('name', 'age',)
    list_filter = ['age']
    search_fields = ['name']
    save_as = True
    inlines = [BookInLineAuthor]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ('name',)
    list_filter = ['name']
    search_fields = ['name']
    save_as = True
    inlines = [BookInLineStore]
    fieldsets = [
        (None, {'fields': ['name']}),
        ]
