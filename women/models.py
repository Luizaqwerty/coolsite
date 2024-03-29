from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Women(models.Model):
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    age = models.IntegerField(default=18)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="women/", null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Women'
        verbose_name_plural = 'Women'