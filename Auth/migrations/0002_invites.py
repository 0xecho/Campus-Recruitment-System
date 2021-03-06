# Generated by Django 2.2.7 on 2019-11-12 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, null=True)),
                ('position', models.CharField(max_length=100)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('from_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.Company')),
                ('to_stud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.Student')),
            ],
        ),
    ]
