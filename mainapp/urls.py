from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage.as_view()),
    path('login/', LoginPage.as_view()),
    path('courses/', CoursesPage.as_view()),
    path('doc/', DocPage.as_view()),
    path('contacts/', ContactsPage.as_view()),
    path('news/', NewsPage.as_view()),
]