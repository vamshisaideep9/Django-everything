# Generated by Django 5.1.4 on 2024-12-25 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="entry",
            name="authors",
            field=models.ManyToManyField(related_name="entries", to="blog.author"),
        ),
        migrations.AlterField(
            model_name="entry",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entries",
                to="blog.blog",
            ),
        ),
    ]