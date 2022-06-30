# Generated by Django 4.0.5 on 2022-06-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
            ],
        ),
    ]
