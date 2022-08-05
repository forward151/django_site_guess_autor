from django.urls import path
from . import views


urlpatterns = [
    path('main_page', views.main_page, name='main_page'),
    path('materials', views.materials, name='materials'),
    path('about', views.about, name='about'),
    path('other', views.other, name='other'),
    path('page_input', views.page_input, name='page_input'),
    path('input_data_file', views.input_data_file, name='input_data_file'),
    path('page_input_ok', views.input_ok, name='page_input_ok'),
    path('page_database', views.page_database, name='page_database'),
    path('input_test', views.input_test, name='input_test'),
    path('Answer', views.answer, name='answer'),
]

