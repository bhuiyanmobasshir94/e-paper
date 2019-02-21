from rest_framework import serializers

from question_model.models import Subject, Paper, Solution


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'


class SolutionIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id',)
