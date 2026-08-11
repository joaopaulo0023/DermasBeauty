from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_service_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeEyebrowServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/eyebrows/', verbose_name='foto')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ordem')),
                ('eyebrow_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.homeeyebrowservice', verbose_name='cartão de sobrancelhas')),
            ],
            options={
                'verbose_name': 'Foto adicional do cartão',
                'verbose_name_plural': 'Fotos adicionais do cartão',
                'ordering': ['order', 'id'],
            },
        ),
    ]
