# Generated by Django 3.1.5 on 2021-03-09 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0003_purchasehistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='date_added',
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.cart'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='jackets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.jackets'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='pants',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.pants'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='shirts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.shirts'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='shoes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ec.shoes'),
        ),
    ]
