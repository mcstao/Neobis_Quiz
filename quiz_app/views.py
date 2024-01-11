import django_filters
from drf_spectacular.utils import extend_schema
from rest_framework import generics, filters as s_filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, ArticleSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, \
    ArticleDetailSerializer, WelcomeSerializer
from .models import Category, Article, Quiz, Question, Answer


@extend_schema(
    description='Этот эндпоинт возвращает категории'
)
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {
            'title': ['icontains'],
            'content': ['icontains'],
            'category__name': ['exact'],
        }


class QuizFilter(django_filters.FilterSet):
    class Meta:
        model = Quiz
        fields = {
            'title': ['icontains'],
            'category__name': ['exact'],
        }


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(
    description='Этот эндпоинт возвращает все статьи'
)
class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend, s_filters.SearchFilter]
    search_fields = ['title', 'content', 'category__name']
    filterset_class = ArticleFilter


@extend_schema(
    description='Этот эндпоинт возвращает определенную статью'
)
class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


@extend_schema(
    description='Этот эндпоинт приветствие квиза'
)
class QuizWelcomeView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = WelcomeSerializer



@extend_schema(
    description='Этот эндпоинт возвращает все квизы'
)
class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = WelcomeSerializer
    filter_backends = [DjangoFilterBackend, s_filters.SearchFilter]
    search_fields = ['title', 'category__name']
    filterset_class = QuizFilter
    pagination_class = CustomPagination

@extend_schema(
    description='Этот эндпоинт возвращает определенный квиз'
)
class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


@extend_schema(
    description='Этот эндпоинт возвращает вопросы квиза'
)
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@extend_schema(
    description='Этот эндпоинт возвращает ответы квиза'
)
class AnswerListView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
