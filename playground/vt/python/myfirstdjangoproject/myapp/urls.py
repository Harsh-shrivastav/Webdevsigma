from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('', views.index, name='index'),
    path('submit_form/', views.submit_form, name='submit_form'), 
    path('show_form/', views.show_form, name='show_form'), 
    path('update_form/<int:id>/', views.update_details, name='update_form'),
    path('update_submit/<int:id>/', views.update_submit, name='update_submit'),
    path('delete_form/<int:id>/', views.delete_form, name='delete_form'),
    path('home/', views.home, name='home'),
    path('sample/', views.sample, name='sample'),  # Add this line for the sample view

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
