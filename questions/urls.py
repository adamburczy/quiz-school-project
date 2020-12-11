from django.urls import path
from questions.views import render_question, correct_answear, incorrect_answear, score, try_again, start

app_name = 'question'

urlpatterns = [
    path('', start, name='start'),
    path('pytanie', incorrect_answear, name='incorrect_answear'),
    path('quiz', correct_answear, name='correct_answear'),
    path('score', score, name='score'),
    path('try-again', try_again, name='try_again')
]