# Generated by Django 3.1.5 on 2021-03-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0018_auto_20210324_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasehistory',
            name='purchase_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
