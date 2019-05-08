from django.contrib import admin

from .models import Article, Page, Category

# A minimal ModelAdmin
# admin.site.register(Category)

class CategoryInline(admin.TabularInline):
    model = Article.categories.through

class BaseContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created','status')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('image_preview', 'modified')
    search_fields = ['title', 'subtitle']


class ArticleAdmin(BaseContentAdmin):
    inlines = (CategoryInline, )
    fieldsets = (
        ( 'Content', {
            'fields': ('title', 'subtitle', 'slug', 'summary', 'body' ),
        }),
        ( 'Main Image', {
            'fields': ('image', 'image_credit', 'width_field', 'height_field', 'image_preview'),
        }),
        ( 'Publishing Options', {
            'fields': ('author', 'status', 'enable_comments', 'created', 'modified'),
        }),
    )

admin.site.register(Article, ArticleAdmin)

class PageAdmin(BaseContentAdmin):
    pass

admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
