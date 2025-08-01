from django.contrib import admin
from .models import Category, SubCategory, Dress, CartItem
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'quantity', 'price', 'total_price', 'added_at')
    search_fields = ('user__username', 'product_name')
    list_filter = ('added_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Dress)
