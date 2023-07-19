from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('app:authordetail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse_lazy('app:authorupdate', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse_lazy('app:authordelete', kwargs={'pk': self.pk})

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.IntegerField()
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, related_name="books")
    cover = models.ImageField("Book cover", upload_to="covers/", blank=True ,help_text="lorem jskauhi ugqywgq vhvahg svcaytsf")
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
    user = models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    books = models.ManyToManyField("Book", verbose_name=(""))

    def __str__(self):
        return f"{self.user} "    