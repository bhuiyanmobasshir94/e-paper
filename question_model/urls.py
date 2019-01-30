
from django.urls import path

from .views import SubjectListAPIView, SolutionDetailAPIView


urlpatterns = [
    path('^subjects/', SubjectListAPIView.as_view()),
    path('solution/<int:id>/',SolutionDetailAPIView.as_view())

]



