# coding: utf-8

#         app: org.toledano.blogApp
#      module: blog.urls
# description: URL patterns form blog app
#      author: Javier Sanchez Toledano
#        date: 2022-08-20
#     licence: MIT
#      python: 3.10

from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views
from .sitemaps import BlogSitemap


sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ads.txt', TemplateView.as_view(template_name='blog/ads.txt', content_type='text/plain')),
    path('robots.txt', TemplateView.as_view(template_name='blog/robots.txt', content_type="text/plain")),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('category/<str:slug>', views.CategoryDetail.as_view(), name='category'),
    path('<str:category>/<str:slug>', views.EntryDetail.as_view(), name='entry'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('archivo.html', views.Archivo.as_view(), name='sitemap'),
    path('cv/', views.CVView.as_view(), name='cv'),
    path('', views.BlogIndex.as_view(), name='index'),
]
