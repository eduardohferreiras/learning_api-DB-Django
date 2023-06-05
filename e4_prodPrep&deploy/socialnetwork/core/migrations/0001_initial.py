# Generated by Django 4.2.1 on 2023-05-26 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('isHidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id1', to='core.profile')),
                ('id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id2', to='core.profile')),
            ],
        ),
    ]