from django.urls import path

from main_app.custom_views.accounts import (
    RegisterView,
    SignupView,
)
from main_app.custom_views.commons import (
    ContactUsView,
    AboutUsView,
    HomePageView,
    AboutView, 
    TermOfUseView,
    PrivacyPolicyView,
    SupportView,
    ContactUsView,
    ComplaintsView,
    FeedbackView,
    ServicesView,

)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
       path('about-us/', AboutView.as_view(), name='about-us'),
    path("term-of-use", TermOfUseView.as_view(), name="term-of-use"),
    path("privacy-policy", PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("support", SupportView.as_view(), name="support"),
    path("contact-us", ContactUsView.as_view(), name="contact-us"),
    path("complaints", ComplaintsView.as_view(), name="complaints"),
    path("feedback", FeedbackView.as_view(), name="feedback"),
    path("services", ServicesView.as_view(), name="services"),
    
    path("sign-up", SignupView.as_view(), name="sign-up"),
    path("register", RegisterView.as_view(), name="register"),
]