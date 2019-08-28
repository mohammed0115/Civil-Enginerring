from django.conf.urls import url
from .views import *
from MusaApp.import_expense import *
from django.urls import path
urlpatterns = [
    path('work/<int:id>', index, name='work'),
    path('buildingWorks/<int:id>', display_BuildingWorks, name="display_buildingWorks"),
    path('NegashaWork/<int:id>', display_NegashaWork, name="display_negashaWork"),
    path('ElectricityWork/<int:id>', display_ElectricityWork, name="display_electricityWork"),
    path('CebakaWork/<int:id>', display_CebakaWork, name="display_CebakaWork"),
    path('BulatWork/<int:id>', display_BulatWork, name="display_BulatWork"),
    path('BayatWork/<int:id>', display_BayatWork, name="display_BayatWork"),
    path('myExpense/<int:id>',indexExpense,name ='myExpense'),
    path('Expense/<int:id>',display_Export,name ='display_Export'),
    path('Import/<int:id>',display_Import,name='display_Import'),
    path('summary/<int:id>',Summary,name='summary'),



    path('add_buildingWorks/<int:id>', add_BuildingWorks, name="add_buildingWorks"),
    path('add_NegashaWork/<int:id>', add_NegashaWork, name="add_negashaWork"),
    path('add_ElectricityWork/<int:id>', add_ElectricityWork, name="add_electricityWork"),
    path('newproject',add_NewProject,name='newproject'),
    path('add_Expense/<int:id>',add_Export,name ='add__Export'),
    path('add_Import/<int:id>',add_Import,name='add__Import'),
    path('add_CebakaWork/<int:id>', add_CebakaWork, name="add_CebakaWork"),
    path('add_BulatWork/<int:id>', add_BulatWork, name="add_BulatWork"),
    path('add_BayatWork/<int:id>', add_BayatWork, name="add_BayatWork"),



    path('buildingWorks/edit_item/<int:pk>', edit_BuildingWorks, name="edit_buildingWorks"),
    path('negashaWork/edit_item/<int:pk>', edit_NegashaWork, name="edit_negashaWork"),
    path('electricityWork/edit_item/<int:pk>', edit_ElectricityWork, name="edit_electricityWork"),
    path('Expense/edit_item/<int:pk>', edit_Export, name="edit_Export"),
    path('Import/edit_item/<int:pk>', edit_Import, name="edit_Import"),
    path('CebakaWork/edit_item/<int:pk>', edit_CebakaWork, name="edit_CebakaWork"),
    path('BulatWork/edit_item/<int:pk>', edit_BulatWork, name="edit_BulatWork"),
    path('BayatWork/edit_item/<int:pk>', edit_BayatWork, name="edit_BayatWork"),


    path('buildingWorks/delete/<int:pk>', delete_BuildingWorks, name="delete_buildingWorks"),
    path('add_negashaWork/delete/<int:pk>', delete_NegashaWork, name="delete_negashaWork"),
    path('electricityWork/delete/<int:pk>', delete_ElectricityWork, name="delete_electricityWork"),
    path('Expense/delete/<int:pk>', delete_Export, name="delete_Export"),
    path('Import/delete/<int:pk>', delete_ElectricityWork, name="delete_Import"),
    path('CebakaWork/delete/<int:pk>', delete_CebakaWork, name="delete_CebakaWork"),
    path('BulatWork/delete/<int:pk>', delete_BulatWork, name="delete_BulatWork"),
    path('BayatWork/delete/<int:pk>', delete_BayatWork, name="delete_BayatWork"),
]
