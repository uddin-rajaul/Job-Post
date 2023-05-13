# Generated by Django 4.1.7 on 2023-04-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_author_jobpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=models.ManyToManyField(to='app.skills'),
        ),
    ]