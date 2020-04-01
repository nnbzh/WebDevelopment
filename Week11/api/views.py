from django.http import JsonResponse, HttpResponse, HttpRequest
from api.models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_single(request, company_id):
    company = Company.objects.get(id = company_id)
    company_json = company.to_json()
    return JsonResponse(company_json, safe=False)

def vacancy_list_by_company(request, company_id):
    vacancies = Vacancy.objects.all(id = company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_by_id(request,vacancy_id):
    vacancies = Vacancy.objects.get(id=vacancy_id)
    vacancies_json = vacancies.to_json()
    return JsonResponse(vacancies_json, safe=False)

def top_ten(request):
    vacancies = Vacancy.objects.all()[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)