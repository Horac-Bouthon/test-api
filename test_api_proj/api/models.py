from django.db import models

# Create your models here.
class PatexData(models.Model):
    classification = models.CharField(max_length=50)
    product_name =   models.CharField(max_length=50)
    image_url = models.CharField(max_length=300, null=True, blank=True)
    description =  models.TextField(
        null=True,
        blank=True,
    )
    features =  models.TextField(
        null=True,
        blank=True,
    )
    tech_url = models.TextField(
        null=True,
        blank=True,
    )
    security_url = models.TextField(
        null=True,
        blank=True,
    )
    bar_code = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {} ({})'.format(self.classification, self.product_name, self.bar_code)
