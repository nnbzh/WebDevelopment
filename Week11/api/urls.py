from django.urls import path
from api.views import company_list, company_single, vacancy_list_by_company, vacancy_list, vacancy_by_id, top_ten
urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_single),
    path('companies/<int:company_id>/vacancies', vacancy_list_by_company),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_by_id),
    path('vacancies/top_ten/', top_ten)
]