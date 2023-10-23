"""
URL configuration for easy_dea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path


## about/fr

urlpatterns = i18n_patterns(
    path("easy-dea-admin/", admin.site.urls),
    path("", include("main_app.urls")),
    path('compte/', include('compte.urls')),
    path('dashboard/', include('dashboard.urls')),
    
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""

from main_app import views

from main_app.custom_views.accounts import (
    RegisterView,
    SignupView,
)

from main_app.views import (
    MyView,
    HomePageView,
    AboutUsView,
    AboutView, 
    TermOfUseView,
    PrivacyPolicyView,
    SupportView,
    ContactUsView,
    ComplaintsView,
    FeedbackView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main_app.urls")),
    path("home/", HomePageView.as_view(), name="home"),

    path('hello/', views.hello),
    path("mine/", MyView.as_view(), name="my-view"),
    
  #  path("about-us/", AboutUsView.as_view(), name="about-us"),
    path('about-us/', AboutView.as_view(), name='about-us'),
    path("term-of-use", TermOfUseView.as_view(), name="term-of-use"),
    path("privacy-policy", PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("support", SupportView.as_view(), name="support"),
    path("contact-us", ContactUsView.as_view(), name="contact-us"),
    path("complaints", ComplaintsView.as_view(), name="complaints"),
    path("feedback", FeedbackView.as_view(), name="feedback"),
    
    path("sign-up", SignupView.as_view(), name="sign-up"),
    path("register", RegisterView.as_view(), name="register"),
    
]
"""

