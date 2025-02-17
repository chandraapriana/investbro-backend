"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/us/', views.post_stock_data, name='postStockData'),
    path('stock/id/', views.post_stock_id_data, name='post_stock_id'), 
    path('crypto/', views.post_crypto_data, name='post_crypto_data_data'), 
    path('gold/', views.post_gold_data, name='post_crypto_data_data'), 
    path('forex/<str:currency1>/<str:currency2>/', views.post_forex_data, name='post_forex_data'),
    path('crypto/ticker-list/', views.get_crypto_ticker_list, name='crypto_ticker_list'),
    path('stock/id/ticker-list/', views.get_id_stock_ticker_list, name='us_stock_ticker_list'),
    path('stock/us/ticker-list/', views.get_us_stock_ticker_list, name='id_stock_ticker_list'),
]
