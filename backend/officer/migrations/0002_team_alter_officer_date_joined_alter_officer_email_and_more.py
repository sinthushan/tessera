# Generated by Django 5.1.4 on 2025-01-19 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='officer',
            name='date_joined',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='officer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='officer.team'),
            preserve_default=False,
        ),
    ]
