# Generated by Django 4.2.9 on 2024-02-02 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clasificados', '0002_alter_anuncio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='telefono',
            field=models.IntegerField(default=58126024),
            preserve_default=False,
        ),
    ]
