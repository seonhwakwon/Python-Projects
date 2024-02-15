from django.db import models

# Create your models here.

#create new model
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default=0, blank=True, null=False)

    #creaate Meta class
    class Meta:
        #if the number of object is  plural, add es.
        verbose_name_plural= "University campuses"

