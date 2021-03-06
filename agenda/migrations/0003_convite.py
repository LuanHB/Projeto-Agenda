# Generated by Django 2.0.2 on 2018-04-02 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0002_compromisso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aceitar', models.BooleanField(default=False)),
                ('compromisso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Compromisso')),
                ('convidados', models.ManyToManyField(related_name='convidados', to=settings.AUTH_USER_MODEL)),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
