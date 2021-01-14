from django.db import models

class TimeStamp(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified' fields.
    """

    created = models.DateTimeField(
        auto_now_add=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        TimeStamp.Meta class designating that his class is abstract 
        and will not be added to the database.
        """
        abstract = True
