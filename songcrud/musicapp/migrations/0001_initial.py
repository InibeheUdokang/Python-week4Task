# Generated by Django 4.1.2 on 2022-10-28 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('Last_name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_released', models.DateField()),
                ('likes', models.IntegerField(default=0)),
                ('artiste_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musicapp.song')),
            ],
        ),
    ]
