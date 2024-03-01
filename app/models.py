from django.db import models

# Create your models here.
class Smartphone(models.Model):
    name = models.CharField(max_length=72)
    company = models.CharField(max_length=36)
    color = models.CharField(max_length=16)
    RAM = models.IntegerField()
    memory = models.IntegerField()
    price = models.FloatField()
    img_url = models.CharField(max_length=124)
    release_date = models.DateField()

    def __str__(self) -> str:
        return self.name
     
    def to_dict(self)->dict:
        return {
            "id":self.id,
            "name":self.name,
            "company": self.company,
            "color": self.color,
            "RAM": self.RAM,
            "memory": self.memory,
            "price": self.price,
            "img_url": self.img_url,
            "release_date": self.release_date
        }