# myapp/urls.py
from django.urls import path
from .views import register, user_login, faq_list, home, user_list

urlpatterns = [
    path('', home, name='home'),  # Home view for the root URL
    path('register/', register, name='register'),  # Registration view
    path('login/', user_login, name='login'),  # Login view
    path('faqs/', faq_list, name='faq_list'),  # FAQ view
    path('users/', user_list, name='user_list'),  # User list view
]
