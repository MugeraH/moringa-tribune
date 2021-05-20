
from django.contrib import admin
from django.urls import path,include,re_path
import django.contrib.auth.urls 
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView


urlpatterns = [
   path('admin/', admin.site.urls),
    re_path(r'',include('news.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    
    path('accounts/register/',
        RegistrationView.as_view(success_url='/'),
        name='django_registration_register'),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), {"next_page": '/login'}),
    # re_path(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/login'})
    # path('tinymce/', include('tinymce.urls'))
  
]

