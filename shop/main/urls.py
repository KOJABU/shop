from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('expensive/', views.expensive,name='expensive' ),
    path('sort1/',views.sort_by_category_mouse,name = 'mouses'),
    path('sort2/', views.sort_by_category_headphones, name='headpgones' ),
    path('item/<int:item_id>/', views.detail, name = 'detail'),
    path('sort1/item/<int:item_id>/', views.detail_sort1, name = 'detail'),
    path('sort2/item/<int:item_id>/', views.detail_sort2, name = 'detail'),
    path('expensive/item/<int:item_id>/', views.detail_exp, name = 'detail'),
    path('add/', views.add_product, name='add')
] 

