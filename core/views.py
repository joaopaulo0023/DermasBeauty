from datetime import date

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .forms import AppointmentForm
from .models import GalleryImage, HomeEyebrowService, HomePageContent, Service, Testimonial


def home(request):
    services = Service.objects.filter(active=True)[:6]
    testimonials = Testimonial.objects.filter(active=True)[:3]
    gallery_images = GalleryImage.objects.filter(active=True).order_by('-created_at')[:3]
    homepage, _ = HomePageContent.objects.get_or_create(pk=1)
    eyebrow_services = HomeEyebrowService.objects.filter(active=True).prefetch_related('images')
    return render(request, 'core/home.html', {
        'services': services,
        'testimonials': testimonials,
        'gallery_images': gallery_images,
        'homepage': homepage,
        'eyebrow_services': eyebrow_services,
    })


def about(request):
    return render(request, 'core/sobre.html')


def services(request):
    services = Service.objects.filter(active=True).order_by('category', 'name')
    return render(request, 'core/servicos.html', {'services': services})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, active=True)
    return render(request, 'core/servico_detail.html', {'service': service})


def gallery(request):
    images = GalleryImage.objects.filter(active=True).order_by('-created_at')
    return render(request, 'core/galeria.html', {'images': images})


def contact(request):
    return render(request, 'core/contato.html')


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:appointment_success')
    else:
        form = AppointmentForm()

    services = Service.objects.filter(active=True).order_by('category', 'name')
    return render(request, 'core/agendamento.html', {'form': form, 'services': services})


def appointment_slots(request):
    selected_date = request.GET.get('date')
    try:
        selected_date = date.fromisoformat(selected_date)
    except (TypeError, ValueError):
        return JsonResponse({'slots': []})

    if selected_date < timezone.localdate():
        return JsonResponse({'slots': []})

    return JsonResponse({'slots': AppointmentForm.available_times(selected_date)})


def appointment_success(request):
    return render(request, 'core/agendamento_sucesso.html')


def robots_txt(request):
    return HttpResponse("User-agent: *\nAllow: /\nSitemap: http://127.0.0.1:8000/sitemap.xml\n", content_type='text/plain')


def sitemap_xml(request):
    services = Service.objects.filter(active=True)
    urls = [
        'http://127.0.0.1:8000/',
        'http://127.0.0.1:8000/sobre/',
        'http://127.0.0.1:8000/servicos/',
        'http://127.0.0.1:8000/galeria/',
        'http://127.0.0.1:8000/contato/',
        'http://127.0.0.1:8000/agendamento/',
    ]
    urls.extend(f'http://127.0.0.1:8000/servicos/{service.slug}/' for service in services)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += f'  <url><loc>{url}</loc></url>\n'
    xml += '</urlset>\n'
    return HttpResponse(xml, content_type='application/xml')
