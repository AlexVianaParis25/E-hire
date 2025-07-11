# Generated by Django 5.2.1 on 2025-05-21 22:06

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_empresa_picture_empresa_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_proposta', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('PD', 'Pendente'), ('AC', 'Aceita'), ('RC', 'Recusada'), ('FN', 'Finalizada')], max_length=2)),
                ('valor_negociado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('prazo_negociado', models.CharField(max_length=50)),
                ('empresa_contratante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='propostas_contratadas', to='business.empresa')),
                ('empresa_prestadora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='propostas_prestadas', to='business.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliazao', models.DateTimeField(default=django.utils.timezone.now)),
                ('comentario', models.TextField()),
                ('nota', models.CharField(choices=[(1, '1 - Péssimo'), (2, '2 - Ruim'), (3, '3 - Regular'), (4, '4 - Bom'), (5, '5 - Excelente')], max_length=1)),
                ('proposta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.proposta')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('preco_estimado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('prazo_estimado', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.categoria')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='proposta',
            name='servico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.servico'),
        ),
    ]
