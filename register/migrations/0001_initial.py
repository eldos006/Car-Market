# Generated by Django 4.1.3 on 2022-11-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Ползователь',
                'verbose_name_plural': 'Ползователи',
            },
        ),
    ]
