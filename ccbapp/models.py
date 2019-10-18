# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TbAuthority(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_project = models.CharField(max_length=20)
    t_code = models.CharField(max_length=20)
    t_name = models.CharField(max_length=20)
    t_belogn = models.CharField(max_length=20)
    t_enable = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_authority'
        unique_together = (('t_project', 't_code'),)


class TbBaseCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_code = models.CharField(unique=True, max_length=20)
    t_detail = models.CharField(max_length=20)
    t_belong = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_base_code'


class TbDepart(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_belong = models.CharField(max_length=20)
    t_code = models.CharField(max_length=20)
    t_name = models.CharField(max_length=20)
    t_sname = models.CharField(db_column='t_SName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_depart'
        unique_together = (('t_belong', 't_code'),)


class TbDepartUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_belong = models.CharField(max_length=20)
    t_depart_id = models.BigIntegerField()
    t_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_depart_user'
        unique_together = (('t_belong', 't_depart_id', 't_user_id'),)


class TbLogin(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_uid = models.CharField(max_length=20)
    t_pwd = models.CharField(max_length=50)
    t_user_id = models.BigIntegerField()
    t_belong = models.CharField(max_length=10)
    t_enable = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_login'
        unique_together = (('t_user_id', 't_belong'), ('t_uid', 't_belong'),)


class TbRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_project = models.CharField(max_length=20)
    t_code = models.CharField(max_length=20)
    t_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_role'
        unique_together = (('t_project', 't_code'),)


class TbRoleGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_project = models.CharField(max_length=20)
    t_role_id = models.BigIntegerField()
    t_user_id = models.BigIntegerField()
    t_depart_id = models.BigIntegerField()
    t_belong = models.CharField(max_length=20)
    t_enable = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_role_group'
        unique_together = (('t_project', 't_role_id', 't_user_id'), ('t_project', 't_role_id', 't_depart_id'),)


class TbUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_name = models.CharField(max_length=20)
    t_sex = models.TextField()  # This field type is a guess.
    t_email = models.CharField(max_length=50)
    t_mobile = models.CharField(max_length=50, blank=True, null=True)
    t_offtel = models.CharField(db_column='t_offTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t_adr = models.CharField(max_length=50, blank=True, null=True)
    t_belong = models.CharField(max_length=10)
    t_enable = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_user'
