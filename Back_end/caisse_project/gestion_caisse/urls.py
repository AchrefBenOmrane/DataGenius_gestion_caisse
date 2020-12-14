from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_list/', views.show_list),
    path('show_list_panier/', views.show_list_panier),
    path('detail_ticket/', views.detail_ticket),
   
   
]
