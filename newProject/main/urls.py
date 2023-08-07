from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.energysaving, name='energy_saving'),
    path('energyefficiency', views.energyefficiency, name='energy_efficiency'),
    path('nuclearenergy', views.nuclearenergy, name='nuclear_energy'),
    path('nucencalc', views.nucencalc, name='calculate_nuclear_energy'),
    path('eneffcalc', views.eneffcalc, name='calculate_energy_efficiency'),
    path('ensavingcalc', views.ensavingcalc, name='energy_saving_calc')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #подключение всех статических файлов