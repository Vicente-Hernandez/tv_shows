from django.db import models
from django.db.models.fields import related

# Manager validador
class NetworksManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['name']) < 3:
            errors["name"] = "Network name should be at least 5 characters"
        return errors

# Create your models here.
class Networks(models.Model):
    name = models.CharField(max_length=255)
    
    #campos de trazabilidad
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = NetworksManager()

# Manager validador
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 3:
            errors["title"] = "Network name should be at least 5 characters"
        
        if len(postData['description']) < 15:
            errors["description"] = "Network description should be at least 15 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.ForeignKey(Networks, related_name='shows', on_delete = models.CASCADE)
    date = models.DateTimeField()
    description =models.CharField(max_length=500)
    
    #campos de trazabilidad
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowsManager()
    
        
    def __repr__(self) -> str:
        return f'{self.id}{self.title}'
