from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=300)
    primarycategory = models.BooleanField(default=False)

    def __str__(self):
     return self.title

class product(models.Model):
    mainimage = models.ImageField(upload_to='online_store/',blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200,verbose_name='preview Text')
    detail_text = models.TextField(max_length=1000,verbose_name='details text')
    price = models.FloatField()

    def __str__(self):
        return self.name

# cart model
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

# ordered items
class Order(models.Model):
    ordered_items = models.ManyToManyField(cart)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username






