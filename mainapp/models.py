from django.db import models
from mainapp.managers.news_manager import NewsManager


class News(models.Model):
    objects = NewsManager()

    title = models.CharField(max_length=256, verbose_name='title')
    preamble = models.CharField(max_length=1024, blank=True, null=True, verbose_name='preamble')
    body = models.TextField(blank=False, null=False, verbose_name='body')
    body_as_markdown = models.BooleanField(
        default=False,
        verbose_name='as_markdown'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date of creating',
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='date of editing',
        editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()


# class SubNews(models.Model):
#     body = models.TextField(blank=True, null=True)
#     news = models.ForeignKey(News, on_delete=models.CASCADE)


class Courses(models.Model):
    name = models.CharField(max_length=256, verbose_name='name')
    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='description'
    )
    description_as_markdown = models.BooleanField(
        default=False,
        verbose_name='as markdown'
    )
    cost = models.DecimalField(
        blank=False,
        null=False,
        decimal_places=2,
        max_digits=20,
        verbose_name='cost'
    )
    cover = models.FilePathField(verbose_name='cover')
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='created'
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='updated'
    )

    def __str__(self):
        return self.name


class Lessons(models.Model):
    course = models.PositiveSmallIntegerField(verbose_name='course')
    num = models.PositiveSmallIntegerField(verbose_name='num')
    title = models.CharField(max_length=64, verbose_name='title')
    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='description'
    )
    description_as_markdown = models.BooleanField(
        default=False,
        verbose_name='as markdown'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='created'
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='updated'
    )

    def __str__(self):
        return f'{self.title}: {self.description}'


class Teachers(models.Model):
    name_first = models.CharField(max_length=128, verbose_name='name_first')
    name_second = models.CharField(max_length=128, verbose_name='name_second')
    day_birth = models.DateField(verbose_name='day_birth')
    course = models.TextField(null=True, verbose_name='course')

    def __str__(self):
        return f'{self.name_first}  {self.name_second}'
