from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from lists import views as lists_views

urlpatterns = [
    path('', lists_views.home_page, name='home'),
    path('lists/', include('lists.urls')),
]
