from django.urls import path
from basic_app import views

# Template taggin
app_name = 'goes_to_html'

urlpatterns=[
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]