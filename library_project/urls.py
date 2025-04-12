from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('transactions/', include('transactions.urls')),


    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),  # default dashboard
]
