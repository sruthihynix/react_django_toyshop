from django.db import models

# Create your models here.
class Toy(models.Model):
    Id = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Image = models.CharField(max_length=200)
    Price = models.IntegerField()
    Qty = models.IntegerField()

    class Meta:
        db_table = "table_toy"