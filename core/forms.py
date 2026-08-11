from django import forms
from django.utils import timezone

from .models import Appointment, Service


class AppointmentForm(forms.ModelForm):
    OPENING_HOURS = tuple(range(9, 19))
    BLOCKING_STATUSES = ('PENDENTE', 'CONFIRMADO')

    class Meta:
        model = Appointment
        fields = [
            'name',
            'phone',
            'email',
            'service',
            'preferred_date',
            'preferred_time',
            'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
            'phone': forms.TextInput(attrs={'placeholder': '(99) 99999-9999'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seuemail@email.com'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.Select(),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Conte um pouco mais sobre o que você deseja'}),
        }
        labels = {
            'name': 'Nome',
            'phone': 'Telefone',
            'email': 'E-mail',
            'service': 'Serviço',
            'preferred_date': 'Data desejada',
            'preferred_time': 'Horário desejado',
            'message': 'Observações',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(active=True).order_by('category', 'name')
        self.fields['service'].empty_label = 'Selecione um serviço'
        self.fields['preferred_date'].widget.attrs['min'] = timezone.localdate().isoformat()
        selected_date = self._selected_date()
        self.fields['preferred_time'].choices = self.time_choices(selected_date)

    def _selected_date(self):
        value = self.data.get('preferred_date') or self.initial.get('preferred_date')
        if not value:
            return None
        try:
            return forms.DateField().clean(value)
        except forms.ValidationError:
            return None

    @classmethod
    def available_times(cls, selected_date, appointment_id=None):
        if not selected_date:
            return []
        occupied = Appointment.objects.filter(
            preferred_date=selected_date,
            status__in=cls.BLOCKING_STATUSES,
        )
        if appointment_id:
            occupied = occupied.exclude(pk=appointment_id)
        occupied_times = {booked.strftime('%H:%M') for booked in occupied.values_list('preferred_time', flat=True)}
        return [
            f'{hour:02d}:00'
            for hour in cls.OPENING_HOURS
            if f'{hour:02d}:00' not in occupied_times
        ]

    @classmethod
    def time_choices(cls, selected_date, appointment_id=None):
        if not selected_date:
            return [('', 'Escolha primeiro a data')]
        available_times = cls.available_times(selected_date, appointment_id)
        if not available_times:
            return [('', 'Não há horários disponíveis nesta data')]
        return [('', 'Selecione um horário')] + [(time, time) for time in available_times]

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data['preferred_date']
        if preferred_date < timezone.localdate():
            raise forms.ValidationError('Escolha uma data de hoje em diante.')
        return preferred_date

    def clean(self):
        cleaned_data = super().clean()
        preferred_date = cleaned_data.get('preferred_date')
        preferred_time = cleaned_data.get('preferred_time')
        if preferred_date and preferred_time:
            available_times = self.available_times(preferred_date, self.instance.pk)
            if preferred_time.strftime('%H:%M') not in available_times:
                self.add_error('preferred_time', 'Este horário acabou de ser reservado. Escolha outro.')
        return cleaned_data
