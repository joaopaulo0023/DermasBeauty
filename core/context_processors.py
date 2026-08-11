from django.conf import settings

from .models import SiteConfiguration


def site_settings(request):
    configuration, _ = SiteConfiguration.objects.get_or_create(
        pk=1,
        defaults={
            'clinic_name': settings.CLINIC_NAME,
            'city': settings.CITY,
            'whatsapp': settings.WHATSAPP,
            'instagram': settings.INSTAGRAM,
            'email': settings.EMAIL,
            'address': settings.ADDRESS,
            'business_hours': settings.BUSINESS_HOURS,
            'google_maps_url': settings.GOOGLE_MAPS_URL,
        },
    )
    return {
        'CLINIC_NAME': configuration.clinic_name,
        'CITY': configuration.city,
        'WHATSAPP': configuration.whatsapp,
        'WHATSAPP_LINK': f'https://wa.me/{configuration.whatsapp}',
        'INSTAGRAM': configuration.instagram,
        'INSTAGRAM_URL': f'https://instagram.com/{configuration.instagram.lstrip("@")}',
        'EMAIL': configuration.email,
        'ADDRESS': configuration.address,
        'BUSINESS_HOURS': configuration.business_hours,
        'GOOGLE_MAPS_URL': configuration.google_maps_url,
    }
