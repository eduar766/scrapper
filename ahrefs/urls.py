from django.contrib import admin
from django.urls import path, include
from . import views
from django_filters.views import FilterView
from django_filters.views import object_filter
from .models import Backlinks
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.pre_index, name='pre_index'),
    path('index', views.index, name='index'),
    path('backlinks/', views.backlinks, name='backlinks'),
    path('backlinks-scrapper/', views.backlinks_scrapper, name='backlinks_scrapper'),
    path('results/', views.bk_results, name='results'),
    path('search-bk/', views.search_bk, name='search_bk'),
    path('list-result/', FilterView.as_view(model=Backlinks)),
    path('foro/', views.search_foro, name='foro'),
    path('excel/', views.export_excel, name='excel'),

    # Single Ahrefs
    path('single-ahrefs/', views.single_ahrefs, name='single_ahrefs'),

    # Search to Google
    path('google/', views.google, name='google'),
    path('google-search/', views.google_search, name='google_search'),
    path('google-results/', views.google_results, name='google_results'),
    path('backlinks-google', views.bk_google_all, name='bk_google_all'),
    path('single-bk-google/<pk>', views.g_single, name='g_single'),
    path('delete-google/', views.delete_google, name='delete_google'),

    # CSV
    path('upload-file/', views.upload_file, name='upload_file'),
    path('search-csv/', views.search_csv, name='search_csv'),
    path('result-csv/', views.result_csv, name='result_csv'),
    path('csv-export/', views.CSV_export_excel, name='CSV_export_excel'),
    path('delete-csv/', views.delete_csv, name='delete_csv'),

    # Delete
    path('delete/', views.delete_backlinks, name='delete'),

    # Account
    ]
