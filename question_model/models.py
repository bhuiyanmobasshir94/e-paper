from django.db import models
from django.conf import settings

# Create your models here.
from django.utils.datetime_safe import datetime


class Subject(models.Model):
    syllabus_code = models.IntegerField(help_text='4 digit unique Syllabus Code', primary_key=True)
    syllabus_title = models.CharField(help_text='Name of the Subject', max_length=100)
    board = models.IntegerField(choices=((1, "Cambridge"),
                                         (2, "Edexcel")),
                                default=1)
    level = models.IntegerField(choices=((1, "O Levels"),
                                         (2, "IGCSE"),
                                         (3, "A Levels")),
                                default=1)

    def __str__(self):
        return self.syllabus_title + " - " + str(self.syllabus_code)


class Paper(models.Model):
    subject = models.ForeignKey(Subject, related_name='papers', on_delete=models.PROTECT)
    season = models.CharField(choices=(('s', "summer"),
                                       ('m', "mid session"),
                                       ('w', "winter")),
                              default='s', max_length=2)
    year = models.IntegerField(help_text="Last two digits of the year of the exam")
    paper = models.IntegerField(help_text="Paper number")
    variant = models.IntegerField("Variant number of the paper")
    number_of_questions = models.IntegerField(help_text="Total number of questions", default=40)

    def __str__(self):
        return str(self.subject) + "_" + str(self.season) + "%02d" % (self.year % 100) + "_sl_" + str(self.paper) + str(
            self.variant)

    class Meta:
        unique_together = ('subject', 'season', 'year', 'paper', 'variant')


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, related_name='chapters', on_delete=models.PROTECT)
    chapter_number = models.IntegerField(help_text="Chapter number according to syllabus")
    chapter_name = models.CharField(help_text="Chapter name (according to syllabus)", max_length=100)

    def __str__(self):
        return str(self.chapter_number) + ". " + str(self.chapter_name)

    class Meta:
        unique_together = ('subject', 'chapter_number')


class Solution(models.Model):
    paper_reference = models.ForeignKey(Paper, related_name='solutions', on_delete=models.PROTECT)
    question_number = models.IntegerField(help_text="Question Number")
    correct_answer = models.CharField(choices=(('A', "A"),
                                               ('B', "B"),
                                               ('C', "C"),
                                               ('D', "D")),
                                      max_length=2)
    solution = models.CharField(help_text="Can use Latex code in solution", max_length=1000)
    file_link = models.FileField(help_text="link to animation/video (optional)", upload_to='solutions/', blank=True)
    difficulty = models.FloatField(help_text="for heuristics")
    chapter_number = models.ForeignKey(Chapter, related_name="chapters", null=True, on_delete=models.SET_NULL)
    flagged_by_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.paper_reference) + '_' + "%02d" % self.question_number

    class Meta:
        unique_together = ('paper_reference', 'question_number')


class Customer(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    avatar = models.FileField(help_text="Choose an avatar", upload_to='avatars/')
    phone = models.CharField(help_text="Enter your phone number using the format +880**********", max_length=14)
    school = models.CharField(help_text="Enter the name your school", max_length=50)
    level = models.IntegerField(choices=((1, "O Levels"),
                                         (2, "IGCSE"),
                                         (3, "A Levels")),
                                help_text="Which level are you currently in?", default=0)
    date_of_birth = models.DateField(help_text="Enter your date of birth")
    registered_on = models.DateField(auto_now_add=True)
    credit = models.IntegerField(default=100)
    social_media_link = models.CharField(max_length=100)
    uncredited_flags = models.IntegerField(default=0)
    credited_flags = models.IntegerField(default=0)

    def __str__(self):
        return self.phone


class License(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, related_name="papers", null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('account', 'paper')

class Flag(models.Model):
    flag_ID = models.IntegerField(primary_key=True, db_index=True)
    user_ID = models.ForeignKey(Customer, related_name="flagger", on_delete=models.CASCADE)
    details = models.CharField(help_text="Details about the mistake", max_length=100)
    resolved = models.BooleanField(default=False)
