# Generated by Django 4.0.4 on 2022-05-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='topic',
            field=models.CharField(default='Тақырыпсыз', max_length=100),
            preserve_default=False,
        ),
    ]
