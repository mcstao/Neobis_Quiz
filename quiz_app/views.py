import django_filters
from rest_framework import generics, filters as s_filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, ArticleSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, \
    ArticleDetailSerializer, WelcomeSerializer
from .models import Category, Article, Quiz, Question, Answer


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


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination
    queryset = Article.objects.all()
    filter_backends = [DjangoFilterBackend, s_filters.SearchFilter]
    search_fields = ['title', 'content', 'category__name']
    filterset_class = ArticleFilter


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = WelcomeSerializer
    filter_backends = [DjangoFilterBackend, s_filters.SearchFilter]
    search_fields = ['title', 'category__name']
    filterset_class = QuizFilter
    pagination_class = CustomPagination


class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
