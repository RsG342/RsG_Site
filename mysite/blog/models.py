from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="опубликовано")


class Post(models.Model):
    STATUS_CHOICES = (
        ("черновик", "Черновик"),
        ("опубликовано", "Опубликовано"),
    )
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(max_length=250, unique_for_date="publish", verbose_name="Слаг")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name="Автор")
    body = RichTextUploadingField(verbose_name="Текст")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Опубликованно")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Созданно")
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="черновик", verbose_name="Статус")
    object = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(verbose_name="Метки")

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ("-publish",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Коментарии")
    name = models.CharField(max_length=80, verbose_name="Имя")
    email = models.EmailField(verbose_name="электронная почта")
    body = models.TextField(verbose_name="Текст коментария")
    created = models.DateTimeField(auto_now=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        ordering = ("created",)
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return "коментарий {} о {}".format(self.name, self.post)
