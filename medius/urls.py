from django.contrib import admin
from django.urls import path, include
# from app import views
# from app.views import RegisterAPI, LoginAPI
# from knox import views as knox_views


admin.site.site_header = "Medius (STAFF LOGIN)"
admin.site.site_title = "LOGIN ONLY OFFICIAL"
admin.site.index_title = "ERP MANNAGEMENT"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

]


