# Generated by Django 3.1.1 on 2020-09-14 12:05

import core.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('numero_conta', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('endereco', models.CharField(max_length=255)),
                ('bloqueio_utr', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cheque', models.CharField(max_length=50, unique=True)),
                ('numero_conta', models.CharField(max_length=100, unique=True)),
                ('valor_cheque', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('codigo_balcao', models.CharField(max_length=100)),
                ('estado_cheque', models.CharField(choices=[('Devolvido', 'Devolvido'), ('Cancelado', 'Cancelado'), ('Regularizado', 'Regularizado')], default='Devolvido', max_length=50)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('dias', models.IntegerField(default=0)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.banco')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('ficheiro', models.FileField(blank=True, null=True, upload_to=core.utils.regularizacao_file_path)),
            ],
        ),
        migrations.CreateModel(
            name='MotivoDevolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=11, unique=True)),
                ('descricao', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Motivo de Devolucao',
                'verbose_name_plural': 'Motivos de Devolucao',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regularizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_regularizacao', models.CharField(choices=[('Cheque', 'Cheque'), ('Numerario', 'Numerario')], max_length=10)),
                ('cheque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cheque')),
                ('documento', models.ManyToManyField(to='core.Documento')),
            ],
            options={
                'verbose_name_plural': 'Regularizacoes',
            },
        ),
        migrations.CreateModel(
            name='Emitente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('numero_conta', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('endereco', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('P', 'Particular'), ('E', 'Empresa')], max_length=1)),
                ('bloqueio_utr', models.BooleanField(default=False)),
                ('assinante', models.ManyToManyField(blank=True, to='core.Assinante')),
                ('telefone', models.ManyToManyField(to='core.Telefone')),
            ],
        ),
        migrations.AddField(
            model_name='cheque',
            name='emitente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.emitente'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='motivo_devolucao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.motivodevolucao'),
        ),
        migrations.AddField(
            model_name='assinante',
            name='telefone',
            field=models.ManyToManyField(to='core.Telefone'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
