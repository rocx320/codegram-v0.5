# Generated by Django 4.1.7 on 2023-03-31 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0011_question_likes_alter_question_date_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 3, 31, 9, 36, 21, 887656, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
