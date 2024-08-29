from django.urls import path
from .views import IndexView, LearnMoreView

app_name = 'core'  # This defines the namespace for this app (Useful to be referenced when working with other apps

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('learn_more/', LearnMoreView.as_view(), name='learn'),
]
