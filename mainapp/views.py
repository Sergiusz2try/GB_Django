from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'


class ContactsPage(TemplateView):
    template_name = 'contacts.html'


class DocPage(TemplateView):
    template_name = 'doc_site.html'


class LoginPage(TemplateView):
    template_name = 'login.html'


class NewsPage(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news_title'] = 'Новость'
        context['description'] = 'Предварительное описание новости'
        context['news_time'] = datetime.now()
        context['range'] = range(5)

        return context


class CoursesPage(TemplateView):
    template_name = 'courses_list.html'


class IndexPage(TemplateView):
    template_name = 'index.html'
