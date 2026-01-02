from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("services/", views.services, name="services"),
    path("services/<slug:service_slug>/", views.service_details, name="service-details"),
    path("our-team/", views.our_team, name="our-team"),
    path("vision-mission/", views.vision_mission, name="vision-mission"),
    path("our-approach/", views.our_approach, name="our-approach"),
    path("contact-us/", views.contact_us, name="contact-us"),
    path("careers/", views.careers, name="careers"),
    path("privacy-policy/", views.privacy_policy, name="privacy-policy"),
    path("terms-of-service/", views.terms_of_service, name="terms-of-service"),
]