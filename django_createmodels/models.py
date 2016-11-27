from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from model_utils import Choices

@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Model(models.Model):
    name = models.CharField(max_length=30)
    inlines = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

#FIXME not sure how to do this
#     inlines = models.ManyToManyField('self', through='Inlines')
# class Inlines(models.Model)
# https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.ManyToManyField.through
# 

@python_2_unicode_compatible
class Field(models.Model):
    TYPE = Choices(
        'BooleanField',
        'CharField',
        'DateTimeField',
        'DateField',
        'ForeignKey',
        'ImageField',
        'IntegerField',
        'NumericField',
        'TextField',
    )
    model = models.ForeignKey('Model')
    name = models.CharField(max_length=30)
    verbose = models.CharField(max_length=200)
    max_length = models.IntegerField(null=True, blank=True)
    type = models.CharField(choices=TYPE, max_length=30)
    is_fk = models.BooleanField()
    reference = models.ForeignKey('Model', null=True, blank=True, related_name='reference')
    is_pk = models.BooleanField()
    allow_null = models.BooleanField()
    allow_blank = models.BooleanField()
    use_for_self = models.BooleanField()
    use_for_ordering = models.BooleanField()
    admin_search = models.BooleanField()
    admin_filter = models.BooleanField()
    admin_list = models.BooleanField()
    default = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "%s . %s" % (self.model, self.name)
