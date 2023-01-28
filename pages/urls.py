from django.urls import path
from .views import AboutusView, HomePageView, LandingPageView
app_name = 'pages'
urlpatterns = [ 
    path('', LandingPageView.as_view(), name='landing'),
    path('home/', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutusView.as_view(), name='about-us'),
]