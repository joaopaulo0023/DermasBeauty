from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_homeeyebrowservice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='video',
            field=models.FileField(blank=True, help_text='Envie um vídeo em MP4 para exibir neste serviço.', null=True, upload_to='services/videos/', verbose_name='vídeo'),
        ),
    ]
