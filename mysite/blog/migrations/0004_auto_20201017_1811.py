# Generated by Django 2.1.5 on 2020-10-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("created",), "verbose_name": "Коментарии", "verbose_name_plural": "Коментарии"},
        ),
        migrations.AlterField(
            model_name="comment",
            name="active",
            field=models.BooleanField(default=True, verbose_name="Активный"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="blog.Post", verbose_name="Коментарии"),
        ),
    ]
