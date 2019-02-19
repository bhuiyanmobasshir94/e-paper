
from django.urls import path

from .views import SubjectListAPIView, SolutionDetailAPIView,PaperListAPIView


urlpatterns = [
    path('subjects/', SubjectListAPIView.as_view()),
    path('subject/<int:syllabus_code>/papers/', PaperListAPIView.as_view()),
    path('paper/<int:paper_pk>/solution/<int:pk>/',SolutionDetailAPIView.as_view())

]



