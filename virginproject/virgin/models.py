from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Cms(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    thumbnail = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "cms"
        verbose_name = "cms"
        verbose_name_plural = "cms"

    def __str__(self):
        return self.title


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "blog"
        verbose_name = "blog"
        verbose_name_plural = "blog"

    def __str__(self):
        return self.blog_title


class Banners(models.Model):
    alt = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "banners"
        verbose_name = "banners"
        verbose_name_plural = "banners"

    def __str__(self):
        return self.alt


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "category"
        verbose_name = "projects category"
        verbose_name_plural = "projects category"

    def __str__(self):
        return self.title


class Projects(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "projects"
        verbose_name = "projects"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    enable_on_home = models.BooleanField(default=False)

    class Meta:
        db_table = "ProductCategory"
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategory"

    def __str__(self):
        return self.title


class ProductCategoryImages(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "ProductCategoryImages"
        verbose_name = "ProductCategoryImages"
        verbose_name_plural = "ProductCategoryImages"

    def __str__(self):
        return self.title


class ProductSubCategory(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    enable_on_home = models.BooleanField(default=False)

    class Meta:
        db_table = "ProductSubCategory"
        verbose_name = "ProductSubCategory"
        verbose_name_plural = "ProductSubCategory"

    def __str__(self):
        return self.title


class ProductSubCategoryImages(models.Model):
    sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "ProductSubCategoryImages"
        verbose_name = "ProductSubCategoryImages"
        verbose_name_plural = "ProductSubCategoryImages"

    def __str__(self):
        return self.title


class Contacted(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = RichTextField()

    class Meta:
        db_table = "contacted"
        verbose_name = "contacted"
        verbose_name_plural = "contacted"

    def __str__(self):
        return 'Name: ' + str(self.name) + ', Email: ' + str(self.email) + ', Message: ' + str(self.message)
