from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ConsVista.views.home', name='home'),
    # url(r'^ConsVista/', include('ConsVista.foo.urls')),
    url(r'^$', 'Aplicacion.views.index'),
    #url(r'^', 'Aplicacion.views.index'),
    url(r'^empleadoNuevo/$', 'Aplicacion.views.empleadoNuevo'),
    url(r'^empleadoLista/$', 'Aplicacion.views.empleadoLista'),
    url(r'^empleadoModelNuevo/$', 'Aplicacion.views.empleadoModelNuevo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
