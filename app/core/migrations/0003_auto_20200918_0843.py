# Generated by Django 3.1.1 on 2020-09-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200918_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emitente',
            name='tipo',
            field=models.CharField(choices=[('P', 'Particular'), ('E', 'Empresa')], max_length=1),
        ),
    ]
