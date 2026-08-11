from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_siteconfiguration'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_eyebrow', models.CharField(default='Dermas Beauty', max_length=120, verbose_name='texto acima do título principal')),
                ('hero_title', models.TextField(default='Realce sua beleza.\nCuide de você.', verbose_name='título principal')),
                ('hero_description', models.TextField(default='Estética & bem-estar para valorizar sua beleza e proporcionar uma experiência de cuidado, autoestima e bem-estar.', verbose_name='descrição principal')),
                ('hero_image', models.ImageField(blank=True, null=True, upload_to='home/', verbose_name='foto do destaque principal')),
                ('experience_title', models.CharField(default='10 anos de experiência', max_length=120, verbose_name='título do destaque')),
                ('experience_text', models.CharField(default='Atendimento com hora marcada • Taubaté/SP', max_length=180, verbose_name='texto do destaque')),
                ('about_eyebrow', models.CharField(default='Sobre a Dermas Beauty', max_length=120, verbose_name='texto acima da seção sobre')),
                ('about_title', models.TextField(default='Sua beleza com cuidado, elegância e acolhimento.', verbose_name='título da seção sobre')),
                ('about_description', models.TextField(default='Na Dermas Beauty, acreditamos que cada pessoa merece sentir-se bem consigo mesma, com autoestima, conforto e resultados que realcem sua identidade. Nossa clínica combina estética, bem-estar e atendimento personalizado em um ambiente acolhedor e sofisticado.', verbose_name='descrição da seção sobre')),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='home/', verbose_name='foto da seção sobre')),
            ],
            options={
                'verbose_name': 'Conteúdo da página inicial',
                'verbose_name_plural': 'Conteúdo da página inicial',
            },
        ),
    ]
