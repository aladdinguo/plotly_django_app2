# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BooksAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBook(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'books_book'


class BooksBookAuthors(models.Model):
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    author = models.ForeignKey(BooksAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)


class BooksBookPublisher(models.Model):
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    publisher = models.ForeignKey('BooksPublisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'books_book_publisher'
        unique_together = (('book', 'publisher'),)


class BooksPublisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'books_publisher'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
        managed = False
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
        managed = False
        db_table = 'equipment_org'
