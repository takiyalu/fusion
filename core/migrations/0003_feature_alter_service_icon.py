# Generated by Django 5.1 on 2024-08-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_employee_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation')),
                ('modified', models.DateField(auto_now=True, verbose_name='Update')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('feature', models.CharField(max_length=100, verbose_name='Feature')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'Cog'), ('lni-stats-up', 'Stats_up'), ('lni-users', 'Users'), ('lni-layers', 'Layers'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket'), ('lni-leaf', 'Leaf'), ('lni-laptop-phone', 'Laptop_phone')], max_length=20, verbose_name='Icon')),
            ],
            options={
                'verbose_name': ('Feature',),
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(choices=[('lni-cog', 'Cog'), ('lni-stats-up', 'Stats_up'), ('lni-users', 'Users'), ('lni-layers', 'Layers'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket'), ('lni-leaf', 'Leaf'), ('lni-laptop-phone', 'Laptop_phone')], max_length=20, verbose_name='Icon'),
        ),
    ]
