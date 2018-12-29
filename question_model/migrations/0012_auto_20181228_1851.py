# Generated by Django 2.1.4 on 2018-12-28 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_model', '0011_auto_20181228_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='subject',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.PROTECT, related_name='papers', to='question_model.Subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solution',
            name='paper_reference',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='solutions', to='question_model.Paper'),
            preserve_default=False,
        ),
    ]
