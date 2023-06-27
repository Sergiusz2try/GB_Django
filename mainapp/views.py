from datetime import datetime
import logging

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import request, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from config import settings

import mainapp.models
from mainapp import forms
from .models import News, Courses
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, View


logger = logging.getLogger(__name__)


class IndexPage(TemplateView):
    template_name = 'main.html'


class ContactsPage(TemplateView):
    template_name = 'contacts.html'


class DocPage(TemplateView):
    template_name = 'doc_site.html'


class NewsListView(ListView):
    model = mainapp.models.News
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = mainapp.models.News
    fields = '__all__'
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(DetailView):
    model = mainapp.models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = mainapp.models.News
    fields = '__all__'
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = mainapp.models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)


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


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        logger.debug("Yet another log message")
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp.models.Courses, pk=pk)

        if not self.request.user.is_anonymous:
            if not mainapp.models.CourseFeedback.objects.filter(
                    course=context["course_object"], user=self.request.user).count():
                context["feedback_form"] = mainapp.forms.CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
            context["feedback_list"] = mainapp.models.CourseFeedback.objects.filter(
                course=context["course_object"]).order_by("-created", "-rating")[:5]

            return context


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp.models.CourseFeedback
    form_class = mainapp.forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/includes/feedback_card.html", context={"item": self.object}
        )
        return JsonResponse({"card": rendered_card})


class MainPage(TemplateView):
    template_name = 'main.html'


class LogView(TemplateView):
    template_name = "mainapp/log_view.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)
        log_slice = []
        with open(settings.LOG_FILE, "r") as log_file:
            for i, line in enumerate(log_file):
                if i == 1000:  # first 1000 lines
                    break
                log_slice.insert(0, line)  # append at start
            context["log"] = "".join(log_slice)
        return context


class LogDownloadView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE, "rb"))