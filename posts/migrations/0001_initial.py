# Generated by Django 2.2.13 on 2020-07-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mortem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=161)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media/')),
                ('body', models.TextField()),
            ],
        ),
    ]