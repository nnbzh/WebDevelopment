from django.urls import path

from api.views import company_list
from api.views.views_cbv import VacancyListApiView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', company_list),
    path('companies/<int:company_id>/vacancies', VacancyListApiView.as_view()),
]