# Generated by Django 3.1.3 on 2021-01-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe_text', models.CharField(max_length=50)),
                ('time_create', models.DateField(auto_now_add=True)),
                ('is_done', models.BooleanField(default=False)),
                ('is_important', models.BooleanField(default=False)),
            ],
        ),
    ]
