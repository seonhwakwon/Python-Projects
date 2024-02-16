# Generated by Django 5.0.2 on 2024-02-16 18:57

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.CharField(max_length=100)),
            ],
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Checkbook.account'),
        ),
    ]
