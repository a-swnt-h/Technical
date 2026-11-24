from django.urls import path
from .views import home,add,edit,delete

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path("edit/<int:id>/",edit,name='edit'),
    path("delete/<int:id>/",delete,name='delete')
]
