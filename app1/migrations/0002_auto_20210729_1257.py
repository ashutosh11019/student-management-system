# Generated by Django 3.2 on 2021-07-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='Convience',
            field=models.CharField(choices=[('None', 'None'), ('Bus', 'Bus'), ('Liberary', 'Liberary'), ('Both', 'Both')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myform',
            name='Std',
            field=models.CharField(choices=[('v', 'v'), ('x', 'x'), ('ii', 'ii'), ('vii', 'vii'), ('i', 'i'), ('iii', 'iii'), ('ix', 'ix'), ('viii', 'viii'), ('vi', 'vi'), ('iv', 'iv')], max_length=50, null=True),
        ),
    ]
