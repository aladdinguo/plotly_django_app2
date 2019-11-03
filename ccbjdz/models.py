# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Worksheet(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalitynumber = models.CharField(db_column='OriginalityNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filloutorganization = models.CharField(db_column='FilloutOrganization', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  # Field name made lowercase.
    writer = models.CharField(db_column='Writer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creativitytype = models.CharField(db_column='CreativityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creativityname = models.CharField(db_column='CreativityName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    creativitylightspot = models.TextField(db_column='CreativityLightspot', blank=True, null=True)  # Field name made lowercase.
    describe = models.TextField(blank=True, null=True)
    modusoperandi = models.TextField(db_column='ModusOperandi', blank=True, null=True)  # Field name made lowercase.
    benefitestimate = models.TextField(db_column='BenefitEstimate', blank=True, null=True)  # Field name made lowercase.
    targetclient = models.CharField(db_column='TargetClient', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sametrade = models.CharField(db_column='SameTrade', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    belongtodepartm = models.CharField(db_column='BelongToDepartm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overallrating = models.CharField(db_column='OverallRating', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transformcategory = models.CharField(db_column='TransformCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transformtime = models.CharField(db_column='TransformTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transformlink = models.CharField(db_column='TransformLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    placeonfile = models.CharField(db_column='PlaceOnFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createidentification = models.CharField(db_column='CreateIdentification', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Worksheet'

