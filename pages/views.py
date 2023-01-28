from django.views.generic import TemplateView

# Create your views here.

class AboutusView(TemplateView):
    template_name = 'pages/about_us.html'

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class LandingPageView(TemplateView):
    template_name = 'pages/landing.html'