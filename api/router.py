from django.urls import path, include

urlpatterns = [
    path("discipline/", include("api.discipline.urls")),
    path("groupp/", include("api.groupp.urls")),
    path("nagr/", include("api.nagr.urls")),
    path("teacher/", include("api.teacher.urls"))

]