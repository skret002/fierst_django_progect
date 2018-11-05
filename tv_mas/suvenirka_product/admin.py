from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
class ColorFieldInline(admin.TabularInline):
    model = ColorField
    extra = 0
    


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline, ColorFieldInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)

class ColorFieldAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ColorField._meta.fields]
   
    class Meta:
        model = ColorField

admin.site.register(ColorField, ColorFieldAdmin)

admin.site.register(IssuesProdukt)

class Description_CategoryAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in Description_Category._meta.fields]
   
    class Meta:
        model = Description_Category

admin.site.register(Description_Category, Description_CategoryAdmin)