from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.TextChoices):
    ADMIN = 'ADMIN', _('Administrator')
    USER = 'USER', _('Default User')
    READ = 'READ', _('Read Only')

class Status(models.TextChoices):
    NEW = 'NEW'
    ACTIVE = 'ACTIVE'
    CLOSED = 'CLOSED'

class Priority(models.IntegerChoices):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    HIGHEST = 3

class Type(models.TextChoices):
    STORY = 'STORY'
    BUG = 'BUG'

class User(models.Model):
    # fields
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.USER)

    def __str__(self):
        return self.name

class Project(models.Model):
    # fields
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_date = models.DateField()
    modified_date = models.DateField()

    def __str__(self):
        return self.title

class Feature(models.Model):
    # foreign keys
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='features')
    
    # fields
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    created_date = models.DateField()
    modified_date = models.DateField()
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.title

class Item(models.Model):
    # foreign keys
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    # fields
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    created_date = models.DateField()
    modified_date = models.DateField()
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.NEW)
    points = models.PositiveIntegerField()
    _type = models.CharField(max_length=5, choices=Type.choices, default=Type.STORY)

    def __str__(self):
        return self.title

class Task(models.Model):
    # foreign keys
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    # fields
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    created_date = models.DateField()
    modified_date = models.DateField()
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    hours_completed = models.PositiveIntegerField()
    hours_left = models.PositiveIntegerField()
    original_estimate = models.PositiveIntegerField()
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.title