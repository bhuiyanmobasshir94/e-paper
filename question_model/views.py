from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from question_model.models import (
    Subject,
    Paper,
    Solution
)
from question_model.serializers import (
    SubjectSerializer,
    PaperSerializer,
    SolutionSerializer,
    SolutionIDSerializer
)


class SubjectListAPIView(ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SolutionDetailAPIView(RetrieveAPIView):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        return Solution.objects.filter(paper_reference_id=self.kwargs['paper_pk'])


class SolutionListAPIView(ListAPIView):
    serializer_class = SolutionIDSerializer

    def get_queryset(self):
        return Solution.objects.filter(paper_reference_id=self.kwargs['paper_pk']).order_by('-id')


class PaperListAPIView(ListAPIView):
    serializer_class = PaperSerializer

    def get_queryset(self):
        filter_set = {
            'subject__syllabus_code':self.kwargs['syllabus_code']
        }
        try:
            year = int(self.request.query_params.get('year'))
            filter_set['year'] = year
        except (ValueError, TypeError):
            pass
        return Paper.objects.filter(**filter_set).order_by('-year')


class YearListAPIView(ListAPIView):

    def get(self, request, *args, **kwargs):
        qs = Paper.objects.filter(subject__syllabus_code
                                    =self.kwargs['syllabus_code']).order_by('-year').values('year').distinct()

        return Response(data=qs)
