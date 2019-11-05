from django.contrib import admin
from .models import Cms, Blog, Category, Projects, ProductCategory,  ProductCategoryImages,  ProductSubCategory, ProductSubCategoryImages, Contacted, Banners

# Register your models here.
admin.site.register(Cms)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Projects)
admin.site.register(ProductCategory)
admin.site.register(ProductCategoryImages)
admin.site.register(ProductSubCategory)
admin.site.register(ProductSubCategoryImages)
admin.site.register(Contacted)
admin.site.register(Banners)


