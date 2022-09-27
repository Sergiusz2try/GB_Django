from django.urls import path
from .views import *
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('login/', LoginPage.as_view(), name='login'),
    path('courses/', CoursesPage.as_view(), name='courses'),
    path('doc/', DocPage.as_view(), name='docs'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('news/', NewsPage.as_view(), name='news'),
]
