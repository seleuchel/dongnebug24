# Generated by Django 2.2.3 on 2019-08-18 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=17, max_digits=20, null=True)),
                ('longitude', models.DecimalField(decimal_places=17, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PushToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
