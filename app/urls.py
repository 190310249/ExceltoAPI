from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('test/', views.test, name = 'test'),
    path('', views.index.as_view(), name = 'index'),
    path('Customerapi/', views.Customerapi.as_view(), name = 'Customerapi'),
    path('excelapi/', views.excelapi.as_view(), name = 'excelapi'),
    path('Branchapi/', views.Branchapi.as_view(), name = 'Branchapi'),
    path('Homeapi/', views.Homeapi.as_view(), name = 'Homeapi'),
    path('Officeapi/', views.Officeapi.as_view(), name = 'Officeapi'),
    path('Loanapi/', views.Loanapi.as_view(), name = 'Loanapi')
    # path('', views.ProductView.as_view(), name="home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
