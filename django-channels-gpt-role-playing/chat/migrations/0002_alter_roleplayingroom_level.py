# Generated by Django 4.2.1 on 2024-06-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleplayingroom',
            name='level',
            field=models.SmallIntegerField(choices=[(1, '초급'), (2, '고급')], default=1, verbose_name='레벨'),
        ),
    ]
