from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    read_time = models.IntegerField(default=15)
    content = models.TextField(max_length=5000)
    art_image = models.ImageField(upload_to='articles/', blank=True, null=True, default='Article image')
    date_created = models.DateTimeField(auto_now_add=True)
    is_archive = models.BooleanField(default=False, verbose_name="Archive status")

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ['id']

    def __str__(self):
        return self.title


class Quiz(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.CASCADE)
    quiz_image = models.ImageField(upload_to='quizzes/', null=True, blank=True, default='Quiz image')
    date_created = models.DateTimeField(auto_now_add=True)
    welcome_page = models.TextField(default=f'Добро пожаловать на квиз по {category}')

    def get_question_count(self):
        return self.question.count()

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    quiz = models.ForeignKey(
        Quiz, related_name='question', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_archive = models.BooleanField(
        default=False, verbose_name=_("Archive Status"))

    def __str__(self):
        return self.title


class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
