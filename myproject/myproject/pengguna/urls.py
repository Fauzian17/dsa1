from django.urls import path

from pengguna.views import(
    home,
    create_formulir,
    formulir_list,
    formulir_view,
    )



urlpatterns = [
    path('', home, name='home'),
    path('formulir/list', formulir_list, name='formulir_list'),
    path('formulir/view/<str:kode_formulir>/', formulir_view, name='formulir_view'),
    path('create/formulir',create_formulir,name='formulir')
]