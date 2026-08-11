from django.db import migrations, models


def create_default_eyebrow_services(apps, schema_editor):
    HomeEyebrowService = apps.get_model('core', 'HomeEyebrowService')
    HomeEyebrowService.objects.bulk_create([
        HomeEyebrowService(title='Design de sobrancelhas', description='Formatação que valoriza o formato do seu rosto e deixa seu olhar mais harmonioso.', order=1),
        HomeEyebrowService(title='Design com henna', description='Realce suave e duradouro para complementar o desenho natural das sobrancelhas.', order=2),
        HomeEyebrowService(title='Brow Lamination', description='Modelagem e definição para um efeito mais alinhado, elegante e uniforme.', order=3),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_homepagecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecontent',
            name='eyebrow_services_eyebrow',
            field=models.CharField(default='Seu olhar merece atenção', max_length=120, verbose_name='texto acima da seção de sobrancelhas'),
        ),
        migrations.AddField(
            model_name='homepagecontent',
            name='eyebrow_services_title',
            field=models.TextField(default='Sobrancelhas com design sofisticado.', verbose_name='título da seção de sobrancelhas'),
        ),
        migrations.CreateModel(
            name='HomeEyebrowService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='título')),
                ('description', models.TextField(verbose_name='descrição')),
                ('image', models.ImageField(blank=True, null=True, upload_to='home/eyebrows/', verbose_name='foto')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ordem')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
            ],
            options={
                'verbose_name': 'Cartão de sobrancelhas da home',
                'verbose_name_plural': 'Cartões de sobrancelhas da home',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.RunPython(create_default_eyebrow_services, migrations.RunPython.noop),
    ]
