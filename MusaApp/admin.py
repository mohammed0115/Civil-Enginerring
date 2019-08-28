from django.contrib import admin
from MusaApp.models import *
from import_export.admin import ImportExportModelAdmin



class BuildingWorksAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    cost=BuildingWorks.total_cost
    fields= ('projectId','details', 'unit', 'amount','flour', 'price')
    list_display =('projectId','details', 'unit', 'amount', 'price','flour','total_cost')
    list_filter=('projectId',  'flour',)
    ordering = ['flour','projectId']
    search_fields = ['details']
class ElectricityWorkAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    cost=BuildingWorks.total_cost
    fields= ('projectId','details', 'unit', 'amount','flour', 'price')
    list_display =('projectId','details', 'unit', 'amount', 'price','flour','total_cost')
    list_filter=('projectId',  'flour',)
    ordering = ['flour','projectId']
    search_fields = ['details']
class NegashaWorkAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    cost=BuildingWorks.total_cost
    fields= ('projectId','details', 'unit', 'amount','flour', 'price')
    list_display =('projectId','details', 'unit', 'amount', 'price','flour','total_cost')
    list_filter=('projectId',  'flour',)
    ordering = ['flour','projectId']
    search_fields = ['details']


class BulatWorkAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    cost=BuildingWorks.total_cost
    fields= ('projectId','details', 'unit', 'amount','flour', 'price')
    list_display =('projectId','details', 'unit', 'amount', 'price','flour','total_cost')
    list_filter=('projectId', 'flour',)
    ordering = ['flour']
    search_fields = ['details']

class CebakaWorkAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    cost=BuildingWorks.total_cost
    fields= ('projectId','details', 'unit', 'amount','flour', 'price')
    list_display =('projectId','details', 'unit', 'amount', 'price','flour','total_cost')
    list_filter=('projectId', 'flour',)
    ordering = ['flour']
    search_fields = ['details']
class BayatWorkAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    cost=BuildingWorks.total_cost
    fields= ('projectId','details', 'unit', 'amount','flour', 'price')
    list_display =('projectId','details', 'unit', 'amount', 'price','flour','total_cost')
    list_filter=('projectId', 'flour',)
    ordering = ['flour']
    search_fields = ['details']

class WorkerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fields= ('projectId','WorkerName',  'Amount', 'dateCreted')
    list_display =('projectId','WorkerName',  'Amount', 'dateCreted')
    list_filter=('projectId', )
    ordering = ['dateCreted']

class ProjectAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fields= ('Name',  'place',)
    list_display =('pk','Name',  'place',)
    ordering = ['Name']
class ExportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fields= ('projectId','details',  'Amount', 'dateCreted')
    list_display =('projectId','details',  'Amount', 'dateCreted')
    list_filter=('projectId',)
    ordering = ['dateCreted']
class ImportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fields= ('projectId','details',  'Amount', 'dateCreted')
    list_display =('projectId','details',  'Amount', 'dateCreted')
    list_filter=('projectId',)
    ordering = ['dateCreted']

admin.site.register(BuildingWorks,BuildingWorksAdmin)
admin.site.register(ElectricityWork,ElectricityWorkAdmin)
admin.site.register(NegashaWork,NegashaWorkAdmin)
admin.site.register(CebakaWork,CebakaWorkAdmin)
admin.site.register(BayatWork,BayatWorkAdmin)
admin.site.register(Worker,WorkerAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Import,ImportAdmin)
admin.site.register(Export,ExportAdmin)
admin.site.register(BulatWork,BulatWorkAdmin)


# Register your models here.
