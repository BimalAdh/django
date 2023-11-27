from django.contrib import admin

# Register your models here
from .models import *
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','brand','stock', 'labels')
    list_filter = ("category", 'brand', 'stock', 'labels')
    search_fields = ("name", 'description')


admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Ad)

#admin.site.register(Brand)
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank')


admin.site.register(Feedback)
admin.site.register(SiteInfo)
#admin.site.register(Product)
admin.site.register(ProductReviews)
admin.site.register(Cart)
