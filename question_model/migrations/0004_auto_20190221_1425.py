# Generated by Django 2.1.7 on 2019-02-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_model', '0003_auto_20190219_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution',
            field=models.TextField(help_text='Can use Latex code in solution', max_length=1000),
        ),
    ]
