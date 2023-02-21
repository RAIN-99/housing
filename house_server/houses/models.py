# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class HousesAlatauskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_alatauskij'


class HousesAlmalinskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_almalinskij'


class HousesAujezovskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_aujezovskij'


class HousesBostandykskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_bostandykskij'


class HousesMedeuskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_medeuskij'


class HousesNauryzbajskiy(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_nauryzbajskiy'


class HousesTurksibskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_turksibskij'


class HousesZhetysuskij(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True, editable=False)
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    floor = models.FloatField(db_column='floor', blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(db_column='total_floor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=512, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'houses_zhetysuskij'

class Predictions(models.Model):
    number_of_rooms = models.CharField(max_length=64, blank=True, null=True)
    floor = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    area = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=128, blank=True, null=True)
    total_floor = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=64, blank=True, null=True)
    prediction =models.FloatField(blank=True, null=True)