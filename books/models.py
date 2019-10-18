from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='出版社名称')
    address = models.CharField(max_length=50, verbose_name='出版社地址')
    city = models.CharField(max_length=60, verbose_name='城市名称')
    state_province = models.CharField(max_length=30, verbose_name='省份名称')
    country = models.CharField(max_length=50, verbose_name='城区名称')
    website = models.URLField(verbose_name='网站地址')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='姓氏')
    last_name = models.CharField(max_length=40, verbose_name='名字')
    email = models.EmailField(blank=True, help_text='这是一个可选字段。填写或者不填写都可以', verbose_name='Email地址')

    def __str__(self):
        return u'%s %s %s' % (self.last_name, self.first_name, self.email)


class Book(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='文章名称')
    authors = models.ManyToManyField(Author, verbose_name='作者名称')
    publisher = models.ManyToManyField(Publisher, verbose_name='出版社名称')
    publication_date = models.DateField(verbose_name='发布日期')

    def __str__(self):
        if self.title:
            # 如果不为空则返回用户名
            return self.title
        else:
            # 如果用户名为空则返回不能为空的对象
            return self.authors


class blog(models.Model):
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=60, verbose_name='博文名称')
    blog_text = models.TextField(verbose_name='博文内容')
    blog_date = models.DateTimeField(verbose_name='日期')

    def __str__(self):
        return self.blog_title
