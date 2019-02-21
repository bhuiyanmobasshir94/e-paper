from rest_framework.generics import ListAPIView, RetrieveAPIView

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

solutions = [
    {
        'latex_string': '\\(\\require{\\gensymb}\\)During the first half of the journey, work is done against gravity. The angle between the direction of the force and displacement 180\\(\\unicode{xb0}\\). So, the work done is \\(-mgh\\). Mathematically,' +
                        '\\begin{align}' +
                        'W_g&=F-g\\dot hd\\\\' +
                        '&=mgh\\cos\\theta\\\\' +
                        '&=mgh\\cos180\\\\' +
                        '&=-mgh' +
                        '\\end{align}',

    },
    {
        'latex_string': '\\begin{align*}' +
                        "P&=\\dfrac{dE}{dt}\\\\" +
                        "&=\\frac{50\\times34\\times10^6}{90}\\\\" +
                        "&=1.89\\times10^7\\\\" +
                        "p&=VI\\\\" +
                        "I&=\\frac{P}{V}\\\\" +
                        "&=\\frac{1.89\\times10^7}{230}\\\\" +
                        "&=8.21\\times10^4" +
                        '\\end{align*}',

    },
    {
        'latex_string': '\\(\\require{\\mhchem}\\)' +
                        "$$\\ce{{}^{237}_{93}Np  ->[\\alpha^{2+}]" +
                        "${\\ce{{}^{233}_{91}Q   ->[\\beta^{-}]}}" +
                        "{\\ce{{}^{233}_{92}R   ->[\\alpha^{2+}]}}" +
                        "{\\ce{{}^{229}_{90}S   ->[\\alpha^{2+}]}}" +
                        "{\\ce{{}^{225}_{88}T   }}$" +
                        '}$$'
    },
    {
        'latex_string': '\\(\\require{\\cancel}\\)\\begin{align*}' +
                        "\\frac{\\mathrm{G.P.E.}}{\\mathrm{work\\ done\\ by}\\ F}&=\\frac{mgh}{Fd}\\\\" +
                        "&=\\frac{mg\\cancel{s}\\sin\\alpha}{F\\cancel{s}}\\\\" +
                        "&=\\frac{mg\\sin\\alpha}{F}" +
                        '\\end{align*}'
    }
]


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
        return Paper.objects.filter(subject__syllabus_code
                                    =self.kwargs['syllabus_code']).order_by('-year')
