from django.urls import path
from blog.views.homepage_views import homepage 


urlpatterns = [
    path('homepage/', homepage),
]
