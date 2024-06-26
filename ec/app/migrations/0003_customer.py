# Generated by Django 5.0.4 on 2024-04-10 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_category_alter_product_prodapp'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('TNG', 'Tanger-Tetouan-Al Hoceima'), ('ORT', 'Oriental'), ('FM', 'Fès-Meknès'), ('RSK', 'Rabat-Salé-Kénitra'), ('BMK', 'Béni Mellal-Khénifra'), ('CS', 'Casablanca-Settat'), ('MS', 'Marrakech-Safi'), ('DT', 'Drâa-Tafilalet'), ('SM', 'Souss-Massa'), ('GON', 'Guelmim-Oued Noun'), ('LSH', 'Laâyoune-Sakia El Hamra'), ('DOE', 'Dakhla-Oued Ed-Dahab')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
