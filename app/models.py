from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.IntegerField()
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name="books")
    cover = VersatileImageField('Book Cover',blank=True,null=True,upload_to="customers/",help_text="size should be more than 100 MB")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('app:bookdetail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('app:bookupdate', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('app:bookdelete', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} ({self.year})"

class FavoriteBook(models.Model):
    user = models.OneToOneField(User, verbose_name=(""),on_delete=models.CASCADE)
    books = models.ManyToManyField("Book", verbose_name=(""))

    def _str_(self):
        return f"{self.user}"
    
    