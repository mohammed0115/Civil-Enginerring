from django.db import models
from django.db.models import Sum
# from ProjectApp.models import Project
# Create your models here.
import datetime
# Create your models here.
class Project(models.Model):
    Name=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    def __str__(self):
        return self.Name   



# class works(models.Model):
#     projectId=models.ForeignKey(Project, on_delete=None)
#     details=models.TextField()
#     unit= models.CharField(max_length=50)
#     amount = models.IntegerField()
#     price = models.FloatField()
#     total_cost=models.FloatField()
#     def calc_total(self):
#         total = (self.price * self.amount) 
#         return total
#     def save(self): 
#         self.total_cost = self.calc_total() 
#         super(works, self).save()  
# 
# 
# 
# 




class Import (models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    Amount=models.FloatField()
    dateCreted=models.DateField(default=datetime.datetime.now,blank=True)



class Export (models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    Amount=models.FloatField()
    dateCreted=models.DateField(default=datetime.datetime.now,blank=True)
    
class Worker (models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    WorkerName=models.CharField(max_length=150)
    Amount=models.FloatField()
    dateCreted=models.DateField(default=datetime.datetime.now,blank=True)
class BuildingWorks(models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    unit= models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField()
    flour= models.IntegerField()
    total_cost=models.FloatField()
    
    def calc_total(self):
        total = (self.price * self.amount) 
        return total
    def save(self): 
        self.total_cost = self.calc_total() 
        super(BuildingWorks, self).save()
class NegashaWork(models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    unit= models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField()
    flour= models.IntegerField()
    total_cost=models.FloatField()
    def calc_total(self):
        total = (self.price * self.amount) 
        return total
    def save(self): 
        self.total_cost = self.calc_total() 
        super(NegashaWork, self).save()
class ElectricityWork(models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    unit= models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField()
    flour= models.IntegerField()
    total_cost=models.FloatField()
    def calc_total(self):
        total = (self.price * self.amount) 
        return total
    def save(self): 
        self.total_cost = self.calc_total() 
        super(ElectricityWork, self).save()
class CebakaWork(models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    unit= models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField()
    flour= models.IntegerField()
    total_cost=models.FloatField()
    def calc_total(self):
        total = (self.price * self.amount) 
        return total
    def save(self): 
        self.total_cost = self.calc_total() 
        super(CebakaWork, self).save()
class BulatWork(models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    unit= models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField()
    flour= models.IntegerField()
    total_cost=models.FloatField()
    def calc_total(self):
        total = (self.price * self.amount) 
        return total
    def save(self): 
        self.total_cost = self.calc_total() 
        super(BulatWork, self).save()
class BayatWork(models.Model):
    projectId=models.ForeignKey(Project, on_delete=None)
    details=models.TextField()
    unit= models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.FloatField()
    flour= models.IntegerField()
    total_cost=models.FloatField()
    def calc_total(self):
        total = (self.price * self.amount) 
        return total
    def save(self): 
        self.total_cost = self.calc_total() 
        super(BayatWork, self).save()

















