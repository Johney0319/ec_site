# Generated by Django 3.1.5 on 2021-03-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0019_purchasehistory_purchase_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasehistory',
            name='purchase_sum',
            field=models.IntegerField(default=1),
        ),
    ]
