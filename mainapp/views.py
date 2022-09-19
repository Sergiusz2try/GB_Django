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


class CoursesPage(TemplateView):
    template_name = 'courses_list.html'

class IndexPage(TemplateView):
    template_name = 'index.html'
