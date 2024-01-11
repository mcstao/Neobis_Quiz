from rest_framework import serializers
from .models import Category, Article, Quiz, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'read_time', 'art_image']


class ArticleDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'content', 'read_time', 'art_image', 'date_created']


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'quiz_image', 'title', 'welcome_page']


class QuizSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'category', 'quiz_image', 'question_count']

    def get_question_count(self, obj):
        return obj.get_question_count()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = [
            'quiz', 'title', 'answer'
        ]
