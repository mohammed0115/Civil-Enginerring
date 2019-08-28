from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
# Create your views here.

from MusaApp.models import *

from MusaApp.forms import *

from django.db.models import  Sum

List={
"BuildingWorks":'أعمال البناء',
"NegashaWork":"أعمال النقاشه",
"CebakaWork":"أعمال السباكه",
"BulatWork":"أعمال البلاط",
"BayatWork":"أعمال البياض",
"ElectricityWork":"أعمال الكهرباء",
}

SummaryList={
"1":"المجموع النهائي لأعمال البناء",
"2":"المجموع النهائي لأعمال النقاشه",
"3":"المجموع النهائي لأعمال السباكه",
"4":"المجموع النهائي لأعمال البلاط",
"5":"المجموع النهائي  لأعمال البياض",
"6":"المجموع النهائي لأعمال الكهرباء",
"7":"المجموع النهائي للنثريات",
"8":"المجموع النهائي للورادات "
}





myid=0
def index(request,id):
    myid=id
    return render(request, 'inv/index.html',context={'id':id})

def display_BuildingWorks(request,id):
    items = BuildingWorks.objects.filter(projectId=id)
    myid=id
   
    context = {
        'items': items,
        'header': 'BuildingWorks',
        'head':List.get('BuildingWorks'),
        'id':id,
        'Total':items.values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
    }
    return render(request, 'inv/index.html', context)


def display_NegashaWork(request,id):
    items = NegashaWork.objects.filter(projectId=id)
    myid=id
    context = {
        'items': items,
        'header': 'NegashaWork',
        'head':List.get('NegashaWork'),
        'id':id,
        'Total':items.values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
    }
    return render(request, 'inv/index.html', context)
#CebakaWork
#BulatWork
#

def display_CebakaWork(request,id):
    items = CebakaWork.objects.filter(projectId=id)
    myid=id
    context = {
        'items': items,
        'header': 'CebakaWork',
        'head':List.get('CebakaWork'),
        'id':id,
        'Total':items.values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
    }
    return render(request, 'inv/index.html', context)

def display_BulatWork(request,id):
    items = BulatWork.objects.filter(projectId=id)
    myid=id
    context = {
        'items': items,
        'header': 'BulatWork',
        'head':List.get('BulatWork'),
        'id':id,
        'Total':items.values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
    }
    return render(request, 'inv/index.html', context)
def display_ElectricityWork(request,id):
    items = ElectricityWork.objects.filter(projectId=id)
    
    myid=id
    context = {
        'items': items,
        'header': 'ElectricityWork',
        'head':List.get('ElectricityWork'),
        'id':id,
        'Total':items.values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
    }
    return render(request, 'inv/index.html', context)

def display_BayatWork(request,id):
    items = BayatWork.objects.filter(projectId=id)
    myid=id
    context = {
        'items': items,
        'header': 'BayatWork',
        'head':List.get('BayatWork'),
        'id':id,
        'Total':items.values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
    }
    return render(request, 'inv/index.html', context)




def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_NewProject(request):
    return add_item(request, ProjectForm)
def add_Expense(request):
    return add_item(request, ExportForm)
def add_BuildingWorks(request,id):
    return add_item(request, BuildingWorksForm)
#CebakaWork
#BulatWork
#BayatWork
def add_CebakaWork(request,id):
    return add_item(request, CebakaWorkForm)
def add_BulatWork(request,id):
    return add_item(request, BulatWorkForm)
def add_BayatWork(request,id):
    return add_item(request, BayatWorkForm)



def add_NegashaWork(request,id):
    return add_item(request, NegashaWorkForm)


def add_ElectricityWork(request,id):
    return add_item(request, ElectricityWorkForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_CebakaWork(request, pk):
    return edit_item(request, pk, CebakaWork, CebakaWorkForm)

def edit_BulatWork(request, pk):
    return edit_item(request, pk, BulatWork,BulatWorkForm)

def edit_BayatWork(request, pk):
    return edit_item(request, pk, BayatWork, BayatWorkForm)




def edit_BuildingWorks(request, pk):
    return edit_item(request, pk, BuildingWorks, BuildingWorksForm)


def edit_NegashaWork(request, pk):
    return edit_item(request, pk, NegashaWork, NegashaWorkForm)

def edit_ElectricityWork(request, pk):
    return edit_item(request, pk, ElectricityWork, ElectricityWorkForm)

def delete_BuildingWorks(request, pk):

    template = 'inv/index.html'
    BuildingWorks.objects.filter(id=pk).delete()

    items = BuildingWorks.objects.all()

    context = {
        'items': items,
        'id':myid,
    }

    return render(request, template, context)


def delete_NegashaWork(request, pk):

    template = 'inv/index.html'
    NegashaWork.objects.filter(id=pk).delete()

    items = NegashaWork.objects.all()

    context = {
        'items': items,
        'id':myid,
    }

    return render(request, template, context)


def delete_ElectricityWork(request, pk):

    template = 'inv/index.html'
    ElectricityWork.objects.filter(id=pk).delete()

    items = ElectricityWork.objects.all()

    context = {
        'items': items,
        'id':myid,
    }

    return render(request, template, context)


def delete_CebakaWork(request, pk):

    template = 'inv/index.html'
    CebakaWork.objects.filter(id=pk).delete()

    items = CebakaWork.objects.all()

    context = {
        'items': items,
        'id':myid,
    }

    return render(request, template, context)



def delete_BulatWork(request, pk):

    template = 'inv/index.html'
    BulatWork.objects.filter(id=pk).delete()

    items = BulatWork.objects.all()

    context = {
        'items': items,
        'id':myid,
    }

    return render(request, template, context)

def delete_BayatWork(request, pk):

    template = 'inv/index.html'
    BayatWork.objects.filter(id=pk).delete()

    items = BayatWork.objects.all()

    context = {
        'items': items,
        'id':myid,
    }

    return render(request, template, context)



def Summary (request,id):
    context={
        "build":BuildingWorks.objects.filter(projectId=id).values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
        "Negasha":NegashaWork.objects.filter(projectId=id).values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
        "Electric":ElectricityWork.objects.filter(projectId=id).values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
        "bayat":BayatWork.objects.filter(projectId=id).values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
        "cebaka":CebakaWork.objects.filter(projectId=id).values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
        "bulat":BulatWork.objects.filter(projectId=id).values('total_cost').distinct().annotate(sum=Sum('total_cost')).aggregate(Sum('sum')),
        "Import":Import.objects.filter(projectId=id).aggregate(Sum('Amount')),
        "Export":Export.objects.filter(projectId=id).aggregate(Sum('Amount')),
        "a1":"المجموع النهائي لأعمال البناء",
        "a2":"المجموع النهائي لأعمال النقاشه",
        "a3":"المجموع النهائي لأعمال السباكه",
        "a4":"المجموع النهائي لأعمال البلاط",
        "a5":"المجموع النهائي  لأعمال البياض",
        "a6":"المجموع النهائي لأعمال الكهرباء",
        "a7":"المجموع النهائي للنثريات",
        "a8":"المجموع النهائي للورادات "
    }
    template = 'project/summary.html'
    return render(request, template, context)