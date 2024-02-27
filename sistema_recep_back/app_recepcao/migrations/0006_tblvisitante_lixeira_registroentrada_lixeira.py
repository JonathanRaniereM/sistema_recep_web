# Generated by Django 4.2.6 on 2024-02-27 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_recepcao', '0005_tblvisitante_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblVisitante_lixeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('assinatura_digital', models.ImageField(blank=True, null=True, upload_to='assinaturas_lixeira/')),
                ('data_hora_exclusao', models.DateTimeField(blank=True, null=True)),
                ('motivo', models.CharField(blank=True, max_length=255, null=True)),
                ('login', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEntrada_lixeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_entrada', models.DateTimeField(blank=True, null=True)),
                ('gabinete', models.CharField(blank=True, max_length=1000, null=True)),
                ('visitante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_recepcao.tblvisitante_lixeira')),
            ],
        ),
    ]