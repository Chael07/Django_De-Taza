# Generated by Django 4.1.3 on 2022-11-14 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('height', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('weight', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('string_no', models.CharField(choices=[('First String', 'First String'), ('Second String', 'Second String')], max_length=100)),
                ('isActive', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Player', to='baseball.person')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.position')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team', to='baseball.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('dorm_latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('dorm_longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
