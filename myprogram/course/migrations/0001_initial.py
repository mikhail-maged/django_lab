# Generated by Django 4.0.5 on 2022-06-30 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='courepertrainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr', models.ManyToManyField(to='course.course')),
                ('ctrainee', models.ManyToManyField(to='trainee.trainee')),
            ],
        ),
    ]