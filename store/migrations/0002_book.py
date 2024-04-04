# Generated by Django 5.0.4 on 2024-04-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_number', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]