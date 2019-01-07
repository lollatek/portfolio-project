# Generated by Django 2.1.4 on 2019-01-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publ_date', models.DateField(auto_now=True)),
                ('summary', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]