# Generated by Django 4.2.4 on 2023-09-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecompleto', models.CharField(max_length=100)),
                ('funcid', models.CharField(max_length=8)),
                ('numerotel', models.CharField(max_length=15)),
            ],
        ),
    ]
