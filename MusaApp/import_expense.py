from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from MusaApp.models import *

from MusaApp.forms import *
from django.db.models import  Sum
List={
"Export":'النثريات ',
"Import":"الواردات ",
}
def indexExpense(request,id):
    return render(request, 'project/ExpenseAndImport.html',context={'id':id})

def display_Export(request,id):
    items = Export.objects.filter(projectId=id)
    context = {
        'items': items,
        'header': 'Export',
        "head":List.get('Export'),
        'id':id,
        'Total':items.aggregate(Sum('Amount'))
    }
    return render(request, 'project/ExpenseAndImport.html', context)


def display_Import(request,id):
    items = Import.objects.filter(projectId=id)
    context = {
        'items': items,
        'header': 'Import',
        "head":List.get('Import'),
        'id':id,
        'Total':items.aggregate(Sum('Amount'))
    }
    return render(request, 'project/ExpenseAndImport.html', context)



def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_Export(request,id):
    return add_item(request, ExportForm)

def add_Import(request,id):
    return add_item(request, ImportForm)

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



def edit_Import(request, pk):
    return edit_item(request, pk, Import, ImportForm)


def edit_Export(request, pk):
    return edit_item(request, pk, Export, ExportForm)

def delete_Export(request, pk):

    template = 'inv/index.html'
    Export.objects.filter(id=pk).delete()

    items = Export.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Import(request, pk):

    template = 'inv/index.html'
    Import.objects.filter(id=pk).delete()

    items = Import.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
