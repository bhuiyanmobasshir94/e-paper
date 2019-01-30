from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from question_model.models import Subject
from question_model.serializers import SubjectSerializer

solutions = [
    {
        'latex_string': 'your string',

    },
    {
        'latex_string': 'my string',

    }
]


class SubjectListAPIView(ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SolutionDetailAPIView(RetrieveAPIView):
    def get(self, request, id, *args, **kwargs):
        return Response(solutions[id])
