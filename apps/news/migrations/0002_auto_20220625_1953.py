# Generated by Django 3.1.6 on 2022-06-25 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='ad',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertising.advertisement'),
        ),
    ]
