from django.urls import path
from .views import get_add, get_all, get_id, brend_item_delete, brend_item_update, smartphone_orderby, smartphone_filter, smartphone_lookup
from .views import contains, icontains, data_in, gt, gte, lt, lte, startswith, endswith, data_range
from .views import get_year, get_month, get_day, get_week, get_week_day, get_quarter, bool_isnull, get_regex
from .views import brend_all, get_brend_name
urlpatterns = [
    path('add/', get_add),
    path('all/', get_all),
    path('id/<int:id>/', get_id),
    path('delete/<int:id>/',brend_item_delete),
    path('update/<int:id>/', brend_item_update),
    path('orderby/', smartphone_orderby),
    path('filter/', smartphone_filter),
    path('lookup/', smartphone_lookup),
    path('contains/', contains),
    path('icontains/', icontains),
    path('in/', data_in),
    path('gt/<int:n>/', gt),
    path('gte/<int:n>/', gte),
    path('lt/<int:n>/', lt),
    path('lte/<int:n>/', lte),
    path('startswith/', startswith),
    path('endswith/', endswith),
    path('range/', data_range),
    path('year/<int:year>/', get_year),
    path('month/<int:month>/', get_month),
    path('day/<int:day>/', get_day),
    path('week/<int:week>/', get_week),
    path('week_day/<int:week_day>/', get_week_day),
    path('quarter/<int:n>/', get_quarter),
    path('isnull/', bool_isnull),
    path('regex/<s>/', get_regex),
    path('<str:brend>/all', brend_all),
    path('brends/', get_brend_name),
   
    
]