"""paiza_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from paiza import views

urlpatterns = [
   path('', views.index, name="index"),
   path('language/<str:key_word>', views.language, name="language"),
   path('frameworks/<str:key_word>', views.frameworks, name="frameworks"),
   path('occupation/<str:key_word>', views.occupation, name="occupation"),
   path('reviews/<str:key_word>', views.reviews, name="reviews"),
   path('job_offers/<str:key_word>', views.job_offers, name="job_offers"),
   path('companys/', views.companys, name="companys")
]
