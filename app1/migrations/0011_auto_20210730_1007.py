# Generated by Django 3.2 on 2021-07-30 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20210730_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='Convience',
            field=models.CharField(choices=[('Liberary', 'Liberary'), ('Both', 'Both'), ('Bus', 'Bus'), ('None', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myform',
            name='Std',
            field=models.CharField(choices=[('iii', 'iii'), ('ix', 'ix'), ('vi', 'vi'), ('ii', 'ii'), ('v', 'v'), ('vii', 'vii'), ('iv', 'iv'), ('x', 'x'), ('viii', 'viii'), ('i', 'i')], max_length=50, null=True),
        ),
    ]
