from django.urls import include, path
from . import views

app_name='accauntant'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]
