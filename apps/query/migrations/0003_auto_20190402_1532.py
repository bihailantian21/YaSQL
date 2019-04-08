# Generated by Django 2.1.7 on 2019-04-02 07:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('query', '0002_auto_20190329_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='MysqlPrivBlacklist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('schema', models.CharField(default='', max_length=128, verbose_name='库名')),
                ('table', models.CharField(default='*', max_length=128, verbose_name='表名')),
                ('columns', models.CharField(default='*', max_length=4096, verbose_name='列名')),
                ('comment', models.CharField(default='', max_length=255, verbose_name='描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='MysqlUserGroupMap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('group', models.CharField(default='', max_length=128, verbose_name='用户组')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mysqlruleschain',
            name='action',
        ),
        migrations.AddField(
            model_name='mysqlruleschain',
            name='columns',
            field=models.CharField(default='*', max_length=4096, verbose_name='列名'),
        ),
    ]