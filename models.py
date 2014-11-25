from django.db import models
from django.contrib.auth.models import User


class Acl_group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % (self.name)


class Employee(models.Model):
    user = models.OneToOneField(User)
    acl_group = models.ForeignKey(Acl_group, default=2)



class Group_1(models.Model):
    name = models.CharField(max_length=200)
    ubn = models.IntegerField(max_length=20)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % (self.name)


class Group_2(models.Model):
    group_1 = models.ForeignKey(Group_1)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Terminal(models.Model):
    group_1 = models.ForeignKey( Group_1)
    group_2 = models.ForeignKey( Group_2, null=True, blank=True)
    name = models.CharField( max_length=200, default='')
    address = models.CharField( max_length=200, default='')
    terminal_no = models.IntegerField( max_length =10, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Terminal_permission(models.Model):
    user = models.ForeignKey(User)
    terminal = models.ForeignKey(Terminal)


