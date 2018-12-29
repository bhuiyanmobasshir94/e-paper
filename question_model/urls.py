from django.conf.urls import url

from .views import SubjectListAPIView


urlpatterns = [
    url(r'^subjects/', SubjectListAPIView.as_view())
]



