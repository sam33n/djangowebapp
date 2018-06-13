# Generated by Django 2.0.4 on 2018-06-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
