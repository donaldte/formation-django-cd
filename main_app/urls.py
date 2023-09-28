from django.urls import path
from .views import create_datesete, DataSetCreationView, modify_dataset, list_dataset, delete_dataset
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

app_name = 'main_app'

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
    
    path('create-dataset/', create_datesete, name='create-dataset'),
    path('modify-dataset/<int:pk>/', modify_dataset, name='modify-data'),
    path('delete-dataset/<int:pk>/', delete_dataset, name='delete-data'),
    path('list-dataset/', list_dataset, name='list-dataset')
    
   # path('create-dataset/', DataSetCreationView.as_view(), name='create-dataset'),
]