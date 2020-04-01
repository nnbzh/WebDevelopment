from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    city = models.CharField(max_length=300)
    address = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name':self.name,
            'description':self.description,
            'address':self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id':self.id,
            'description':self.description,
            'salary':self.description,
            'company_id':self.company_id
        }
