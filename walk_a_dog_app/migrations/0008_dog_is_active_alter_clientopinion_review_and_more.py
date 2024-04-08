# Generated by Django 4.0.4 on 2022-05-29 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('walk_a_dog_app', '0007_remove_clientopinion_data_walk_lat_walk_lng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='clientopinion',
            name='review',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='dog',
            name='avatar',
            field=models.ImageField(blank=True, default='dogs/logo.png', null=True, upload_to='dogs/'),
        ),
        migrations.CreateModel(
            name='TrainerOpinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raport', models.TextField(max_length=250)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client2', to=settings.AUTH_USER_MODEL)),
                ('dog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='walk_a_dog_app.dog')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
