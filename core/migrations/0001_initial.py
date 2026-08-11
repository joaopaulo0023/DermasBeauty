from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('category', models.CharField(choices=[('SOBRANCELHAS', 'Sobrancelhas'), ('FACIAL', 'Facial'), ('MASSAGENS', 'Massagens'), ('CORPORAL', 'Corporal'), ('AMBIENTE', 'Ambiente'), ('RESULTADOS', 'Resultados')], default='RESULTADOS', max_length=30)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Imagem da galeria',
                'verbose_name_plural': 'Imagens da galeria',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.CharField(choices=[('SOBRANCELHAS', 'Sobrancelhas'), ('FACIAL', 'Facial'), ('MASSAGENS', 'Massagens'), ('CORPORAL', 'Corporal'), ('PROCEDIMENTOS_ESTETICOS', 'Procedimentos Estéticos')], max_length=30)),
                ('description', models.TextField()),
                ('benefits', models.TextField(blank=True)),
                ('duration', models.CharField(default='45 min', max_length=60)),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Depoimento',
                'verbose_name_plural': 'Depoimentos',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.TimeField()),
                ('message', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('CONFIRMADO', 'Confirmado'), ('CANCELADO', 'Cancelado'), ('CONCLUIDO', 'Concluído')], default='PENDENTE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='core.service')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
                'ordering': ['-created_at'],
            },
        ),
    ]
