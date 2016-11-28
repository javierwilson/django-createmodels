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
    verbose_name = models.CharField(max_length=200, null=True, blank=True)
    list_per_page = models.IntegerField(null=True, blank=True)
    inlines = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.name, len(self.field_set.all()), )

    def _get_ordering(self):
        return Field.objects.filter(model=self, use_for_ordering=True)
    ordering = property(_get_ordering)

    def _get_selves(self):
        return Field.objects.filter(model=self, use_for_self=True)
    selves = property(_get_selves)

    def _get_admin_list(self):
        return Field.objects.filter(model=self, admin_list=True)
    admin_list = property(_get_admin_list)

    def _get_admin_filter(self):
        return Field.objects.filter(model=self, admin_filter=True)
    admin_filter = property(_get_admin_filter)

    def _get_admin_readonly(self):
        return Field.objects.filter(model=self, admin_readonly=True)
    admin_readonly = property(_get_admin_readonly)

    def _get_admin_search(self):
        return Field.objects.filter(model=self, admin_search=True)
    admin_search = property(_get_admin_search)

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
        'DecimalField',
        'ForeignKey',
        'ImageField',
        'IntegerField',
        'TextField',
    )
    model = models.ForeignKey('Model')
    name = models.CharField(max_length=30)
    verbose_name = models.CharField(max_length=200, null=True, blank=True)
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
    admin_readonly = models.BooleanField()
    default = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "%s . %s" % (self.model, self.name)

    def _get_options(self):
        options = ''
        if self.type == 'ForeignKey':
            options += "'%s', " % (self.reference.name,)

        if self.type == 'CharField' and self.max_length:
            options += "max_length=%s, " % (self.max_length)

        if self.type == 'DecimalField':
            options += 'max_digits=10, decimal_places=2, '

        if self.allow_null:
            options += 'null=True, '

        if self.allow_blank:
            options += 'blank=True, '

        return options

    options = property(_get_options)
