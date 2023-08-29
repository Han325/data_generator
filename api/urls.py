from django.urls import path

from . import views

urlpatterns = [
    path('generate/<int:count>', views.generate_data, name='generate_data'),
    path('query/', views.query_data, name='query_data'),
    path('generate_mongo/<int:count>', views.generate_data_mongo, name='generate_mongo'),
    path('query_mongo/', views.query_data_mongo, name='query_mongo'),
]

