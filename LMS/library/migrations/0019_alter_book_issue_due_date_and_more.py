# Generated by Django 4.0.3 on 2022-12-29 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20220910_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 5, 19, 52, 12, 241238), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book_number',
            field=models.PositiveIntegerField(help_text='Book number for books of the save kind', null=True),
        ),
    ]
