# Generated by Django 4.1.2 on 2022-11-23 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0003_alter_equipo_id_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantencion',
            name='problema_mantencion',
            field=models.TextField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id_ticket',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
