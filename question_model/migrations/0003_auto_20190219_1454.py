# Generated by Django 2.1.5 on 2019-02-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_model', '0002_auto_20190118_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution',
            field=models.CharField(help_text='Can use Latex code in solution', max_length=1000),
        ),
    ]
