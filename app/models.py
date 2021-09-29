from django.db import models
from uuid import uuid4

functions_choices = [
    ('Harvest', 'Harvest'),
    ('Pruning', 'Pruning'),
    ('Scouting', 'Scouting'),
    ('Other', 'Other'),
]


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Worker(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    function = models.CharField(
        max_length=255, choices=functions_choices, default='Other'
    )

    class Meta:
        db_table = 'workers'
        ordering = ['id']
