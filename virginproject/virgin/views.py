from django.shortcuts import render, redirect

from virgin.forms import ContactedForm
from .models import Cms, Blog, Projects, Category, ProductCategory, ProductCategoryImages, ProductSubCategory, Banners, \
    ProductSubCategoryImages


# Create your views here.


def index(request):
    banners = Banners.objects.all()
    products1 = ProductCategory.objects.get(enable_on_home=True, id=1)
    products2 = ProductCategory.objects.get(enable_on_home=True, id=2)
    products3 = ProductCategory.objects.get(enable_on_home=True, id=3)
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()

    return render(request, 'index.html', {'banners': banners, 'products1': products1, 'products2': products2,
                                          'products3': products3, 'about': about, 'contact': con,
                                          'product_header': product_header, 'product_sub_header': product_sub_header})


def productcategory(request, id):
    cms = ProductCategory.objects.get(id=id)
    product = ProductCategoryImages.objects.filter(category_id=id)
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    return render(request, 'productcategory.html', {'product': product, 'cms': cms, 'about': about, 'contact': con,
                                                    'product_header': product_header,
                                                    'product_sub_header': product_sub_header})


def productsubcategory(request, id):
    cms = ProductSubCategory.objects.get(id=id)
    product = ProductSubCategoryImages.objects.filter(sub_category_id=id)
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    return render(request, 'productcategory.html', {'product': product, 'cms': cms, 'about': about, 'contact': con,
                                                    'product_header': product_header,
                                                    'product_sub_header': product_sub_header})


def about(request):
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    cms = Cms.objects.get(id=1)
    return render(request, 'about.html', {'about': cms, 'contact': con,
                                          'product_header': product_header,
                                          'product_sub_header': product_sub_header})


def projects(request):
    cms = Cms.objects.get(id=3)
    pog = Projects.objects.filter().order_by('-id')
    cat = Category.objects.filter().order_by('id')
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    return render(request, 'projects.html', {'projects': pog, 'cms': cms, 'cat': cat, 'about': about, 'contact': con,
                                             'product_header': product_header,
                                             'product_sub_header': product_sub_header})


def contact(request):
    about = Cms.objects.get(id=1)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    con = Cms.objects.get(id=2)
    return render(request, 'contact.html', {'about': about, 'contact': con,
                                            'product_header': product_header,
                                            'product_sub_header': product_sub_header})


def blog(request):
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    cms = Cms.objects.get(id=4)
    blog = Blog.objects.filter().order_by('-id')
    return render(request, 'blog.html', {'blog': blog, 'cms': cms, 'about': about, 'contact': con,
                                         'product_header': product_header,
                                         'product_sub_header': product_sub_header})


def blogdetail(request, id):
    about = Cms.objects.get(id=1)
    con = Cms.objects.get(id=2)
    product_header = ProductCategory.objects.all()
    product_sub_header = ProductSubCategory.objects.all()
    cms = Cms.objects.get(id=4)
    blog = Blog.objects.get(id=id)
    return render(request, 'blog-detail.html', {'blog': blog, 'cms': cms, 'about': about, 'contact': con,
                                                'product_header': product_header,
                                                'product_sub_header': product_sub_header})


def send(request):
    if request.method == "POST":
        form = ContactedForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact/')
    else:
        return render(request, "virgin/contact.html")


def sendhome(request):
    if request.method == "POST":
        form = ContactedForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            request.session["homeform"] = "done"
            return redirect('/')
    else:
        return render(request, "virgin/contact.html")
