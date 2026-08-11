from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=120, verbose_name='nome da clínica')),
                ('city', models.CharField(max_length=120, verbose_name='cidade/UF')),
                ('whatsapp', models.CharField(help_text='Use apenas números, incluindo 55 e o DDD.', max_length=30, verbose_name='WhatsApp')),
                ('instagram', models.CharField(help_text='Exemplo: @dermasbeauty', max_length=120, verbose_name='Instagram')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('address', models.CharField(max_length=255, verbose_name='endereço')),
                ('business_hours', models.CharField(max_length=255, verbose_name='horário de atendimento')),
                ('google_maps_url', models.URLField(verbose_name='URL do Google Maps')),
            ],
            options={
                'verbose_name': 'Configuração do site',
                'verbose_name_plural': 'Configurações do site',
            },
        ),
    ]
