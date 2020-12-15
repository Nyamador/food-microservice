import uuid
from django.db import models

# Create your models here.
class Order(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.PositiveIntegerField()
    food = models.PositiveIntegerField()
    date_added = models.DateField("Date Added", auto_now_add=True)

    def __str__(self):
        return f"#{id}"