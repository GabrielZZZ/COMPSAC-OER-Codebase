from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('instructionPage/', views.instruction, name='instruction'),
    path('choose_scenario/', views.choose_scenario, name='choose_scenario'),
    path('questions/', views.questions, name='questions'),
    path('results/', views.results, name='results'),
    path('welcome/', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
    
    path('mrp_intro/', views.mrp_intro, name='mrp_intro'),
    path('mr_generation_tutorial/', views.mr_generation_tutorial, name='mr_generation_tutorial'),
    path('mr_generation_template/', views.mr_generation_template, name='mr_generation_template'),
    
    path('ads_introduction/', views.ads_introduction, name='ads_introduction'),
    path('standard_scenario_introduction/', views.standard_scenario_introduction, name='standard_scenario_introduction'),
    path('standard_scenario_structure/', views.standard_scenario_structure, name='standard_scenario_structure'),
    path('scenario_resultPage/', views.scenario_resultPage, name='scenario_resultPage'),

    path('quiz/', views.quiz_view, name='quiz_view'),
    
    
]

# Add a URL pattern for serving static files during development
# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

