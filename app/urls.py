from django.urls import path
from .views import get_add, get_all, get_id, brend_item_delete, brend_item_update, smartphone_orderby, smartphone_filter, smartphone_lookup
urlpatterns = [
    path('add/', get_add),
    path('all/', get_all),
    path('id/<int:id>/', get_id),
    path('delete/<int:id>/',brend_item_delete),
    path('update/<int:id>/', brend_item_update),
    path('orderby/', smartphone_orderby),
    path('filter/', smartphone_filter),
    path('lookup/', smartphone_lookup),
    

]