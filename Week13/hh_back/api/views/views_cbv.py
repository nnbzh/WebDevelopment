from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.models import Vacancy
from api.serializers import VacancySerializer

@permission_classes((IsAuthenticated, ))
class VacancyListApiView(APIView):
    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company_id = company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
