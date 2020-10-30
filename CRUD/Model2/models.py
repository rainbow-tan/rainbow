from django.db import models


class DataTable(models.Model):
    auto_id = models.AutoField(primary_key=True)
    field30 = models.CharField(max_length=200)
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field23 = models.CharField(max_length=200)
    field31 = models.CharField(max_length=200)
    field32 = models.CharField(max_length=200)
    field33 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field34 = models.CharField(max_length=200)
    field35 = models.CharField(max_length=200)
    field36 = models.CharField(max_length=200)
    field37 = models.CharField(max_length=200)
    field38 = models.CharField(max_length=200)
    field39 = models.CharField(max_length=200)
    field40 = models.CharField(max_length=200)
    field41 = models.CharField(max_length=200)
    field42 = models.CharField(max_length=200)
    field43 = models.CharField(max_length=200)
    field44 = models.CharField(max_length=200)
    field45 = models.CharField(max_length=200)


class Field36Table(models.Model):
    auto_id = models.AutoField(primary_key=True)
    field1 = models.CharField(max_length=200)


class Field37Table(models.Model):
    auto_id = models.AutoField(primary_key=True)
    field1 = models.CharField(max_length=200)


class Field41Table(models.Model):
    auto_id = models.AutoField(primary_key=True)
    field1 = models.CharField(max_length=200)


class Field42Table(models.Model):
    auto_id = models.AutoField(primary_key=True)
    field1 = models.CharField(max_length=200)
