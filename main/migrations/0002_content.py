# Generated by Django 5.1.1 on 2025-01-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tili', models.CharField(choices=[('Python', 'Python'), ('Golang', 'Golang'), ('Java Script', 'JS'), ('Bat', 'Bat')], max_length=50)),
                ('nomi', models.CharField(max_length=60)),
                ('izoh', models.TextField()),
                ('turlari', models.CharField(choices=[('Phishing', 'Phishing'), ('DOS', 'DOS'), ('DDOS', 'DDOS'), ('Malware', 'Malware'), ('SQL Injection', 'SQL Injection')], max_length=50)),
            ],
        ),
    ]
