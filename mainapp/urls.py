from django.urls import path

from mainapp.views import *
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('courses/', CoursesPage.as_view(), name='courses'),
    path('doc/', DocPage.as_view(), name='docs'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('news/', NewsPage.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailsPageView.as_view(), name='news_details')
]
