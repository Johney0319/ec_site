# Generated by Django 3.1.5 on 2021-03-09 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0006_auto_20210309_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasehistory',
            old_name='cart',
            new_name='cart_history',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='cart_item',
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='pants_history',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.pants'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='shirts_history',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.shirts'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='shoes_history',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.shoes'),
        ),
    ]
