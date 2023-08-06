from django.urls import path
from .views import CategoryList, CategoryCreate, CategoryEdit, CategoryDelete


urlpatterns = [
    path('list/', CategoryList.as_view()),
    path('create/', CategoryCreate.as_view()),
    path('edti/<int:pk>/', CategoryEdit.as_view()),
    path('delete/<int:pk>/', CategoryDelete.as_view()),
]