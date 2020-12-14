# Generated by Django 3.0.4 on 2020-12-14 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_caisse', '0002_auto_20201214_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='pictureUrl',
            field=models.CharField(db_column='pictureUrl', max_length=1000),
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_caisse.caisse')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
    ]