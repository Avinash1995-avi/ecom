from django.contrib import admin
from shop.models import Products, Orders


# Display fields inside the Porducts model
class ProductAdmin(admin.ModelAdmin):
    # customize action list
    def change_category_to_default(self, request, queryset):
        queryset.update(category = 'default')

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ['title']
    actions = ('change_category_to_default',)

    # Display only certain fields
    fields = ('title','price',)
    list_editable = ('price','category')

# Admin customization, Header, Site header and its title
admin.site.site_header = 'E Commerce Site'
admin.site.site_title = 'ABC Shopping'
admin.site.index_title = "Manage ABC Shopping"


# Register your models here.
admin.site.register(Products, ProductAdmin)
admin.site.register(Orders)