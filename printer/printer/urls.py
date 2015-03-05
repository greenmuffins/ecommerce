from django.conf.urls import include, url
from oscar.app import application
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from printer import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'', include(application.urls)),
    url(r'^home/', TemplateView.as_view(template_name="printer/home.html")),
] 