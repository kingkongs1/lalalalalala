import asyncio

from django.db import models


# Create your models here.
class Azureex(models.Model):
    연번 = models.FloatField(blank=True,  primary_key=True)
    종류 = models.CharField(max_length=255, blank=True, null=True)
    종별 = models.CharField(max_length=255, blank=True, null=True)
    지정번호 = models.CharField(max_length=255, blank=True, null=True)
    지정일자 = models.DateTimeField(blank=True, null=True)
    문화재명 = models.CharField(max_length=255, blank=True, null=True)
    소재지 = models.CharField(max_length=255, blank=True, null=True)
    관리주체 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'azureex$'


'''class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        '''