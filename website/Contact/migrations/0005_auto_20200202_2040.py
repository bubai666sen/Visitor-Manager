# Generated by Django 2.2 on 2020-02-02 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0004_sitecontacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteContacts',
            new_name='SiteContact',
        ),
    ]
