from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('TNG', 'Tanger-Tetouan-Al Hoceima'),
    ('ORT', 'Oriental'),
    ('FM', 'Fès-Meknès'),
    ('RSK', 'Rabat-Salé-Kénitra'),
    ('BMK', 'Béni Mellal-Khénifra'),
    ('CS', 'Casablanca-Settat'),
    ('MS', 'Marrakech-Safi'),
    ('DT', 'Drâa-Tafilalet'),
    ('SM', 'Souss-Massa'),
    ('GON', 'Guelmim-Oued Noun'),
    ('LSH', 'Laâyoune-Sakia El Hamra'),
    ('DOE', 'Dakhla-Oued Ed-Dahab'),
)

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Acceptting', 'Acceptting'),
    ('Packed', 'Packed'),
    ('On The Way ', 'On The Way'),
    ('Delivred', 'Delivred'),
    ('Cancel', 'Cancel'),
)



# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)  # Correction de max_lenght à max_length
    selling_price = models.FloatField()  # Correction de Floatfield à FloatField
    discounted_price = models.FloatField()  # Correction de Floatfield à FloatField
    description = models.TextField()
    composition = models.TextField(default='')  # Correction de Textfield à TextField
    prodapp = models.TextField(default='') 
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2,default='')  # Correction de max_lenght à max_length
    product_image = models.ImageField(upload_to='product')

    def __str__(self):  # Correction de _str_ à __str__
        return self.title

class Customer(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    locality = models.CharField(max_length=200)

    city = models.CharField(max_length=50)

    mobile = models. IntegerField(default=0)

    zipcode = models. IntegerField()

    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def str (self):

      return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

class Wishlist(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Mettre à jour le coût total avant de sauvegarder l'objet
        self.total_cost = self.quantity * self.product.discounted_price
        super().save(*args, **kwargs)