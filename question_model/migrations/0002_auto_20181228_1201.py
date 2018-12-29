# Generated by Django 2.1.4 on 2018-12-28 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField(choices=[(1, 's'), (2, 'm'), (3, 'w')], default=1)),
                ('year', models.IntegerField(help_text='Year when the exam was conducted')),
                ('paper', models.IntegerField(help_text='Paper number')),
                ('variant', models.IntegerField(verbose_name='Variant number of the paper')),
                ('number_of_questions', models.IntegerField(help_text='Total number of questions')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='papers', to='question_model.Subject')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='paper',
            unique_together={('subject', 'season', 'year', 'paper', 'variant')},
        ),
    ]
