from django.urls import path

from mainapp.views import *
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('courses/', CoursesPage.as_view(), name='courses'),
    path('courses/<int:pk>/', CoursesDetailView.as_view(), name='courses_detail'),
    path('course_feedback', CourseFeedbackFormProcessView.as_view(), name='course_feedback'),
    path('doc/', DocPage.as_view(), name='docs'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/Detail', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete'),
    path("log_view/", LogView.as_view(), name="log_view"),
    path("log_download/", LogDownloadView.as_view(), name="log_download"),
]
