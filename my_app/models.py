from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'

class List(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    notify_by_email = models.BooleanField(default=False)

class Item(models.Model):
    list_id = models.ForeignKey("List", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    image_url = models.CharField(max_length=80)
    current_price = models.IntegerField()
    desired_price = models.IntegerField()

    def serializable(self):
        return {
            "id": self.id,
            "user_id": self.user.item,
            "list_id": self.list_id.item,
            "name": self.name,
            "image_url": self.image_url,
            "current_price": self.current_price,
            "desired_price": self.desired_price
        }
