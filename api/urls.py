from . import views
from django.urls import path

urlpatterns = [
    path('',views.apiBase,name='api-base'),
    path('questions/',views.questions,name='api-questions'),
    path('all_questions/',views.allquestions,name='api-all-questions'),
    path('question_to_predict/',views.to_predict,name='api-to-predict'),
    path('predict/',views.predict,name='predict'),
]
