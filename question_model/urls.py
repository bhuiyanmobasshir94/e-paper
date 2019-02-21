
from django.urls import path

from .views import (
    SubjectListAPIView,
    SolutionListAPIView,
    SolutionDetailAPIView,
    PaperListAPIView
)


urlpatterns = [
    path('subjects/', SubjectListAPIView.as_view()),
    path('subject/<int:syllabus_code>/papers/', PaperListAPIView.as_view()),
    path('paper/<int:paper_pk>/solutions', SolutionListAPIView.as_view()),
    path('paper/<int:paper_pk>/solution/<int:pk>/',SolutionDetailAPIView.as_view())

]



