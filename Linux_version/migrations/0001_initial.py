# Generated by Django 2.2.3 on 2019-09-29 14:30

import Linux_version.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='开发者账号')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('p12_file', models.FileField(upload_to=Linux_version.models.p12_path, verbose_name='P12文件路径')),
                ('used_device_count', models.IntegerField(default=0, verbose_name='已使用设备数量')),
            ],
            options={
                'verbose_name': '开发者账号',
                'verbose_name_plural': '开发者账号',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('has_confirmed', models.BooleanField(default=False, verbose_name='是否确认')),
                ('buy_devices_count', models.IntegerField(default=0, verbose_name='购买下载量')),
                ('registration_datetime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'ordering': ['-registration_datetime'],
            },
        ),
        migrations.CreateModel(
            name='UDID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=64, null=True, verbose_name='设备型号')),
                ('udid', models.CharField(max_length=128, verbose_name='设备UDID')),
                ('request_distribution_url', models.CharField(blank=True, max_length=240, null=True, verbose_name='请求的分发链接')),
                ('request_datetime', models.DateTimeField(auto_now_add=True, verbose_name='请求时间')),
                ('deveploer_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Linux_version.DeveloperAccount', verbose_name='重签的开发者账号')),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Linux_version.UserInfo', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': 'IOS设备信息',
                'verbose_name_plural': 'IOS设备信息',
                'ordering': ['-request_datetime'],
            },
        ),
        migrations.CreateModel(
            name='IpaPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaupload_path', models.FileField(upload_to=Linux_version.models.user_directory_path, verbose_name='文件相对路径')),
                ('absolute_path', models.CharField(blank=True, max_length=256, null=True, verbose_name='文件绝对路径')),
                ('display_name', models.CharField(default='Not Found App Name', max_length=64, verbose_name='App名称')),
                ('bundid_before', models.CharField(blank=True, max_length=128, null=True, verbose_name='原Bundle ID')),
                ('bundid_after', models.CharField(blank=True, max_length=128, null=True, verbose_name='重签后Bundle ID')),
                ('version', models.CharField(blank=True, max_length=32, null=True, verbose_name='版本')),
                ('appid_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='AppID名称')),
                ('distribution_url', models.URLField(blank=True, null=True, verbose_name='分发链接')),
                ('file_size', models.FloatField(blank=True, default=0.0, null=True, verbose_name='文件大小(M)')),
                ('installed_amount', models.IntegerField(blank=True, default=0, null=True, verbose_name='安装数量')),
                ('upload_datetime', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Linux_version.UserInfo', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': 'IPA包信息',
                'verbose_name_plural': 'IPA包信息',
                'ordering': ['-upload_datetime'],
            },
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, verbose_name='确认码')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='生成时间')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Linux_version.UserInfo', verbose_name='用户')),
            ],
            options={
                'verbose_name': '邮件确认码',
                'verbose_name_plural': '邮件确认码',
                'ordering': ['-c_time'],
            },
        ),
    ]
