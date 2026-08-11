from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('SOBRANCELHAS', 'Sobrancelhas'),
        ('FACIAL', 'Facial'),
        ('MASSAGENS', 'Massagens'),
        ('CORPORAL', 'Corporal'),
        ('PROCEDIMENTOS_ESTETICOS', 'Procedimentos Estéticos'),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField()
    benefits = models.TextField(blank=True)
    duration = models.CharField(max_length=60, default='45 min')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    video = models.FileField('vídeo', upload_to='services/videos/', blank=True, null=True, help_text='Envie um vídeo em MP4 para exibir neste serviço.')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:service_detail', args=[self.slug])


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADO', 'Confirmado'),
        ('CANCELADO', 'Cancelado'),
        ('CONCLUIDO', 'Concluído'),
    ]

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f'{self.name} - {self.service or "Serviço não informado"}'


class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.client_name


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('SOBRANCELHAS', 'Sobrancelhas'),
        ('FACIAL', 'Facial'),
        ('MASSAGENS', 'Massagens'),
        ('CORPORAL', 'Corporal'),
        ('AMBIENTE', 'Ambiente'),
        ('RESULTADOS', 'Resultados'),
    ]

    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='RESULTADOS')
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Imagem da galeria'
        verbose_name_plural = 'Imagens da galeria'

    def __str__(self):
        return self.title


class SiteConfiguration(models.Model):
    clinic_name = models.CharField('nome da clínica', max_length=120)
    city = models.CharField('cidade/UF', max_length=120)
    whatsapp = models.CharField('WhatsApp', max_length=30, help_text='Use apenas números, incluindo 55 e o DDD.')
    instagram = models.CharField('Instagram', max_length=120, help_text='Exemplo: @dermasbeauty')
    email = models.EmailField('e-mail')
    address = models.CharField('endereço', max_length=255)
    business_hours = models.CharField('horário de atendimento', max_length=255)
    google_maps_url = models.URLField('URL do Google Maps')

    class Meta:
        verbose_name = 'Configuração do site'
        verbose_name_plural = 'Configurações do site'

    def __str__(self):
        return 'Configurações do site'


class HomePageContent(models.Model):
    hero_eyebrow = models.CharField('texto acima do título principal', max_length=120, default='Dermas Beauty')
    hero_title = models.TextField('título principal', default='Realce sua beleza.\nCuide de você.')
    hero_description = models.TextField(
        'descrição principal',
        default='Estética & bem-estar para valorizar sua beleza e proporcionar uma experiência de cuidado, autoestima e bem-estar.',
    )
    hero_image = models.ImageField('foto do destaque principal', upload_to='home/', blank=True, null=True)
    experience_title = models.CharField('título do destaque', max_length=120, default='10 anos de experiência')
    experience_text = models.CharField('texto do destaque', max_length=180, default='Atendimento com hora marcada • Taubaté/SP')
    about_eyebrow = models.CharField('texto acima da seção sobre', max_length=120, default='Sobre a Dermas Beauty')
    about_title = models.TextField('título da seção sobre', default='Sua beleza com cuidado, elegância e acolhimento.')
    about_description = models.TextField(
        'descrição da seção sobre',
        default='Na Dermas Beauty, acreditamos que cada pessoa merece sentir-se bem consigo mesma, com autoestima, conforto e resultados que realcem sua identidade. Nossa clínica combina estética, bem-estar e atendimento personalizado em um ambiente acolhedor e sofisticado.',
    )
    about_image = models.ImageField('foto da seção sobre', upload_to='home/', blank=True, null=True)
    eyebrow_services_eyebrow = models.CharField('texto acima da seção de sobrancelhas', max_length=120, default='Seu olhar merece atenção')
    eyebrow_services_title = models.TextField('título da seção de sobrancelhas', default='Sobrancelhas com design sofisticado.')

    class Meta:
        verbose_name = 'Conteúdo da página inicial'
        verbose_name_plural = 'Conteúdo da página inicial'

    def __str__(self):
        return 'Conteúdo da página inicial'


class HomeEyebrowService(models.Model):
    title = models.CharField('título', max_length=120)
    description = models.TextField('descrição')
    image = models.ImageField('foto', upload_to='home/eyebrows/', blank=True, null=True)
    order = models.PositiveSmallIntegerField('ordem', default=0)
    active = models.BooleanField('ativo', default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Cartão de sobrancelhas da home'
        verbose_name_plural = 'Cartões de sobrancelhas da home'

    def __str__(self):
        return self.title


class HomeEyebrowServiceImage(models.Model):
    eyebrow_service = models.ForeignKey(
        HomeEyebrowService,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='cartão de sobrancelhas',
    )
    image = models.ImageField('foto', upload_to='home/eyebrows/')
    order = models.PositiveSmallIntegerField('ordem', default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Foto adicional do cartão'
        verbose_name_plural = 'Fotos adicionais do cartão'

    def __str__(self):
        return f'Foto de {self.eyebrow_service.title}'
