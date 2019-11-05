# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Sheet1(models.Model):
    data = models.CharField(max_length=255, blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)
    similarity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Sheet1'


class Worksheet(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalitynumber = models.CharField(db_column='OriginalityNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filloutorganization = models.CharField(db_column='FilloutOrganization', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  # Field name made lowercase.
    writer = models.CharField(db_column='Writer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creativitytype = models.CharField(db_column='CreativityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creativityname = models.CharField(db_column='CreativityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creativitylightspot = models.TextField(db_column='CreativityLightspot', blank=True, null=True)  # Field name made lowercase.
    describe = models.TextField(blank=True, null=True)
    modusoperandi = models.TextField(db_column='ModusOperandi', blank=True, null=True)  # Field name made lowercase.
    benefitestimate = models.TextField(db_column='BenefitEstimate', blank=True, null=True)  # Field name made lowercase.
    targetclient = models.CharField(db_column='TargetClient', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sametrade = models.CharField(db_column='SameTrade', max_length=1000, blank=True, null=True)  # Field name made lowercase.
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

class EquipmentInfo2(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    heading_code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    system_type = models.CharField(max_length=32, blank=True, null=True)
    clien_version = models.CharField(max_length=32, blank=True, null=True)
    system_version = models.CharField(max_length=32, blank=True, null=True)
    brand = models.CharField(max_length=64, blank=True, null=True)
    unit_type = models.CharField(max_length=64, blank=True, null=True)
    device_state = models.CharField(max_length=32, blank=True, null=True)
    communal = models.CharField(max_length=32, blank=True, null=True)
    pri = models.CharField(max_length=32, blank=True, null=True)
    jailbreak = models.CharField(max_length=32, blank=True, null=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    organization_code = models.CharField(max_length=32, blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    activity = models.CharField(max_length=32, blank=True, null=True)
    free_space = models.CharField(max_length=32, blank=True, null=True)
    activation_date = models.DateTimeField(blank=True, null=True)
    scan_date = models.DateTimeField(blank=True, null=True)
    online = models.CharField(max_length=32, blank=True, null=True)
    ip_group = models.CharField(max_length=32, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    last_online_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.CharField(max_length=32, blank=True, null=True)
    deleter = models.CharField(max_length=32, blank=True, null=True)
    missing = models.CharField(max_length=32, blank=True, null=True)
    creator = models.CharField(max_length=32, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    mender = models.CharField(max_length=32, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    serial_number = models.CharField(max_length=64, blank=True, null=True)
    equipment_number = models.CharField(max_length=32, blank=True, null=True)
    affiliation = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'equipment_info2'


class EquipmentOrg(models.Model):
    insid = models.CharField(primary_key=True, max_length=50)
    inst_chn_fullnm = models.CharField(max_length=50, blank=True, null=True)
    inst_chn_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    inst_hier_cd = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl7_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl7_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl6_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl6_inst_fullnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl6_inst_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl6_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl5_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl5_inst_fullnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl5_inst_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl5_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl4_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl4_inst_fullnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl4_inst_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl4_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl3_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl3_inst_fullnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl3_inst_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl3_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl2_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl2_inst_fullnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl2_inst_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lvl2_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    blng_lv1_insid = models.CharField(max_length=50, blank=True, null=True)
    blng_lv1_inst_fullnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lv1_inst_shrtnm = models.CharField(max_length=50, blank=True, null=True)
    blng_lv1_inst_tpcd = models.CharField(max_length=50, blank=True, null=True)
    oprlinst_min_instpcd = models.CharField(max_length=50, blank=True, null=True)
    cntn_vrtl_inst_ind = models.CharField(max_length=50, blank=True, null=True)
    stdt = models.CharField(max_length=50, blank=True, null=True)
    eddt = models.CharField(max_length=50, blank=True, null=True)
    multi_tenancy_id = models.CharField(max_length=50, blank=True, null=True)
    br_splt_idr = models.CharField(max_length=50, blank=True, null=True)
    data_udt_dt = models.CharField(max_length=50, blank=True, null=True)
    fistload_bsn_dt = models.CharField(max_length=50, blank=True, null=True)
    etl_fistload_script_nm = models.CharField(max_length=50, blank=True, null=True)
    etl_udt_script_nm = models.CharField(max_length=50, blank=True, null=True)
    rep_num_rcrd = models.CharField(max_length=50, blank=True, null=True)
    rcrd_del_dt = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'equipment_org'
