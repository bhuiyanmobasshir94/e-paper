
from rest_framework.generics import ListAPIView

from question_model.models import Subject
from question_model.serializers import SubjectSerializer


class SubjectListAPIView(ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()