from datetime import datetime

from django.http import request
from django.shortcuts import get_object_or_404

from .models import News, Courses
from django.core.paginator import Paginator
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
    paginated_by = 3

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get(
            'page',
            1
        )
        paginator = Paginator(News.objects.all(), self.paginated_by)
        page = paginator.get_page(page_number)

        context = super().get_context_data(**kwargs)

        context['page'] = page

        return context


class NewsDetailsPageView(TemplateView):
    template_name = ''

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news_obj'] = get_object_or_404(News, pk=pk)

        return context


class CoursesPage(TemplateView):
    template_name = 'courses_list.html'
    paginated_by = 3

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get(
            'page',
            1
        )
        paginator = Paginator(Courses.objects.all(), self.paginated_by)
        page = paginator.get_page(page_number)

        context = super().get_context_data(**kwargs)

        context['page'] = page

        return context


class IndexPage(TemplateView):
    template_name = 'index.html'
