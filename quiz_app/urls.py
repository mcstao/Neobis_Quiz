from django.urls import path

from .views import CategoryListView, ArticleListView, QuizListView, QuestionListView, AnswerListView, QuizDetailView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/int:pk/', ArticleListView.as_view(), name='article-detail'),
    path('quiz/', QuizListView.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('answers/', AnswerListView.as_view(), name='answer-list'),
]