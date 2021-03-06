# Generated by Django 2.1 on 2019-03-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0002_question'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='past_contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('contestID', models.ManyToManyField(to='Contest.contest')),
                ('userID', models.ManyToManyField(to='User.user')),
            ],
        ),
    ]
