# Generated by Django 3.1.4 on 2021-01-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Contact_Details',
            },
        ),
    ]