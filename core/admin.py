from django.contrib import admin

from .models import Appointment, GalleryImage, HomeEyebrowService, HomeEyebrowServiceImage, HomePageContent, Service, SiteConfiguration, Testimonial


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'duration', 'active', 'created_at')
    list_filter = ('category', 'active')
    search_fields = ('name', 'description')
    ordering = ('category', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone', 'service_name', 'preferred_date', 'preferred_time', 'status')
    list_filter = ('status', 'preferred_date', 'service')
    search_fields = ('name', 'phone', 'email', 'service__name')
    ordering = ('preferred_date', 'preferred_time')
    date_hierarchy = 'preferred_date'

    def client_name(self, obj):
        return obj.name

    def service_name(self, obj):
        return obj.service.name if obj.service else 'N/A'

    client_name.short_description = 'Cliente'
    service_name.short_description = 'Serviço'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'active', 'created_at')
    list_filter = ('active', 'rating')
    search_fields = ('client_name', 'text')
    ordering = ('-created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'active', 'created_at')
    list_filter = ('category', 'active')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fields = (
        'clinic_name', 'city', 'whatsapp', 'instagram', 'email', 'address',
        'business_hours', 'google_maps_url',
    )

    def has_add_permission(self, request):
        return not SiteConfiguration.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Destaque principal', {
            'fields': ('hero_eyebrow', 'hero_title', 'hero_description', 'hero_image'),
        }),
        ('Cartão de experiência', {
            'fields': ('experience_title', 'experience_text'),
        }),
        ('Seção sobre', {
            'fields': ('about_eyebrow', 'about_title', 'about_description', 'about_image'),
        }),
        ('Seção de sobrancelhas', {
            'fields': ('eyebrow_services_eyebrow', 'eyebrow_services_title'),
        }),
    )

    def has_add_permission(self, request):
        return not HomePageContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class HomeEyebrowServiceImageInline(admin.TabularInline):
    model = HomeEyebrowServiceImage
    extra = 1
    fields = ('image', 'order')


@admin.register(HomeEyebrowService)
class HomeEyebrowServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'active')
    list_editable = ('order', 'active')
    search_fields = ('title', 'description')
    ordering = ('order', 'id')
    inlines = (HomeEyebrowServiceImageInline,)
