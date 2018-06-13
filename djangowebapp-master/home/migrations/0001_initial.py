# Generated by Django 2.0.4 on 2018-06-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('slug', models.SlugField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]