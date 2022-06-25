# Generated by Django 3.1.6 on 2022-06-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('logo', models.ImageField(upload_to='static/spoonsers/')),
                ('ad_link', models.URLField()),
                ('ad_text', models.TextField(max_length=1000)),
            ],
        ),
    ]