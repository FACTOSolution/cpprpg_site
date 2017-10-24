# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_functions', '0025_merge_20170919_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pronome_tratamento',
            field=models.CharField(choices=[('Senhor', 'Senhor'), ('Senhora', 'Senhora'), ('Senhorita', 'Senhorita'), ('Doutor', 'Doutor'), ('Doutora', 'Doutora')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='modalidade',
            field=models.CharField(choices=[('GRA', 'Estudante de Graduacao'), ('PRO', 'Profissional')], default=False, max_length=3),
        ),
    ]
