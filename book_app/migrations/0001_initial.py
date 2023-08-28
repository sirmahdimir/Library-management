# Generated by Django 4.2.4 on 2023-08-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
                ('date_of_release', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'Books',
            },
        ),
    ]
