# Generated by Django 4.2.14 on 2024-08-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resumeprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('skills', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('sslc', models.CharField(blank=True, max_length=200, null=True)),
                ('hss', models.CharField(blank=True, max_length=200, null=True)),
                ('grduation', models.CharField(blank=True, max_length=200, null=True)),
                ('projecttitle', models.CharField(blank=True, max_length=200, null=True)),
                ('projectdescription', models.CharField(blank=True, max_length=200, null=True)),
                ('experience', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
