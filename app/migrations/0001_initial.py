# Generated by Django 3.0.6 on 2020-06-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=20)),
            ],
        ),
    ]
