import json

from django.http import JsonResponse

from api.models import Company, Vacancy
from api.serializers import CompanySerilizer, VacancySerializer

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerilizer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def vacancy_list_by_company(request, company_id):
    vacancies = Vacancy.objects.all(id = company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


# def company_single(request, company_id):
#     company = Company.objects.get(id = company_id)
#     company_json = company.to_json()
#     return JsonResponse(company_json, safe=False)
#
# def vacancy_list(request):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json, safe=False)
#
# def vacancy_by_id(request,vacancy_id):
#     vacancies = Vacancy.objects.get(id=vacancy_id)
#     vacancies_json = vacancies.to_json()
#     return JsonResponse(vacancies_json, safe=False)
#
# def top_ten(request):
#     vacancies = Vacancy.objects.all()[:10]
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json, safe=False)