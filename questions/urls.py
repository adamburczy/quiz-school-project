from django.urls import path
from questions.views import render_question1, correct_answear1, incorrect_answear1, score, try_again, start, test, incorrect_answear2, correct_answear2, incorrect_answear3, correct_answear3, incorrect_answear4, correct_answear4, incorrect_answear5, correct_answear5, incorrect_answear6, correct_answear6, incorrect_answear7, correct_answear7,incorrect_answear8, correct_answear8, incorrect_answear9, correct_answear9, incorrect_answear10, correct_answear10

app_name = 'question'

urlpatterns = [
    path('', start, name='start'),
    path('pytanie1/', render_question1, name='question1'),
    #path('pytanie2/', render_question2, name='question2'),
    path('pytanie', incorrect_answear1, name='incorrect_answear1'),
    path('wdan2321', incorrect_answear2, name='incorrect_answear2'),
    path('382971', incorrect_answear3, name='incorrect_answear3'),
    path('3898971', incorrect_answear4, name='incorrect_answear4'),
    path('3897971', incorrect_answear5, name='incorrect_answear5'),
    path('342321', incorrect_answear6, name='incorrect_answear6'),
    path('3432971', incorrect_answear7, name='incorrect_answear7'),
    path('3894571', incorrect_answear8, name='incorrect_answear8'),
    path('3893471', incorrect_answear9, name='incorrect_answear9'),
    path('3896771', incorrect_answear10, name='incorrect_answear10'),
    path('quiz', correct_answear1, name='correct_answear1'),
    path('39284729', correct_answear2, name='correct_answear2'),
    path('47294', correct_answear3, name='correct_answear3'),
    path('177294', correct_answear4, name='correct_answear4'),
    path('1745294', correct_answear5, name='correct_answear5'),
    path('39211729', correct_answear6, name='correct_answear6'),
    path('456294', correct_answear7, name='correct_answear7'),
    path('177594', correct_answear8, name='correct_answear8'),
    path('1732294', correct_answear9, name='correct_answear9'),
    path('1732784', correct_answear10, name='correct_answear10'),
    path('score', score, name='score'),
    path('try-again', try_again, name='try_again')
]

