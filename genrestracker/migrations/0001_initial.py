# Generated by Django 2.1.1 on 2018-10-04 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='UserGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='genrestracker.Genre')),
            ],
        ),
    ]