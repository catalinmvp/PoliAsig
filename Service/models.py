from django.db import models

# Create your models here.
class Service(models.Model):
    Serv_id=models.DecimalField(max_digits=3,decimal_places=0)
    description=models.TextField(default='add a description')

    def getid(self):
        return self.Serv_id
    def getdesc(self):
        return self.description