from django.urls import path, include
from . import views
urlpatterns = [
    # path('',views.HomeView.as_view(), name='home'),
    path('save/',views.CreateView.as_view(), name='save'),
    path('delete/',views.DeleteView.as_view(), name='delete'),
    path('edit/',views.UpdateView.as_view(), name="edit"),
    path('', views.DataTableView.as_view(), name='home'),
    
    
]