from api.models import Company
from api.serializers import CompanySerilizer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerilizer(companies, many=True)
        return Response(serializer.data)
