import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    cost = models.IntegerField(default=0)
    slug = models.SlugField()
    is_private = models.BooleanField()
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
class Staff(models.Model):
    staff_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    image_url = models.URLField()
    name = models.CharField(max_length=64)
    company_position = models.CharField(max_length=64)
    review = models.TextField(default="-")
    
