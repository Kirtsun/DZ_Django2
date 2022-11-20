from django.contrib import admin

from .models import Author, Quote


class QuoteInLine(admin.TabularInline):
    model = Quote
    extra = 3


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fieldsets = [
        (None, {'fields': ['name']})]
    inlines = [QuoteInLine]
    list_display_links = ('name', )
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20
    save_as = True


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("quote",)
    fieldsets = [
        (None, {'fields': ['quote']}),
        ('Authors', {'fields': ['author']})
    ]
    list_filter = ['author']
    search_fields = ['quote']
    list_per_page = 20
    save_as = True
