# Generated by Django 3.2.18 on 2023-03-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_auto_20230302_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=100)),
                ('adob', models.DateField()),
                ('aage', models.CharField(max_length=50)),
            ],
        ),
    ]
