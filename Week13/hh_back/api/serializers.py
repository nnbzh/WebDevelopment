from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True);
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=300)

    def create(self, validated_data):
        company = Company()
        company.name = validated_data.get('name', 'default name');
        company.description = validated_data.get('description', 'default description')
        company.save()
        return company


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company_id')
