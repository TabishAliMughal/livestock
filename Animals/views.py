from django.shortcuts import render , redirect
from Animals.forms import AnimalForm , AnimalExpenceForm , AnimalProductForm , AnimalGroupsForm
from Animals.models import AnimalTypes , Animal , AnimalExpences , AnimalProducts , AnimalGroups
from Farm.models import Farm


def List(request , slug=None):
    type = "Animal"
    groups = AnimalGroups.objects.all()
    types = []
    if slug:
        type = AnimalTypes.objects.get(slug = slug)
        animals = Animal.objects.filter(type = type)
    else:
        animals = Animal.objects.all()
    if len(request.session.get('nav')) > 1:
        types = request.session.get('nav')
    else:
        type = AnimalTypes.objects.get(slug = request.session.get('nav')[0]['slug'])
    context = {
        'animals' : animals ,
        'groups' : groups ,
        'type' : type ,
        'types' : types ,
    }
    return render(request , 'Animals/List.html' , context)

def Detail(request , pk):
    animal = Animal.objects.get(id = pk)
    expences = AnimalExpences.objects.filter(animal = pk)
    products = AnimalProducts.objects.filter(animal = pk)
    context = {
        'animal' : animal ,
        'expences' : expences ,
        'products' : products ,
    }
    return render(request , 'Animals/Detail.html' , context)

def Create(request , type=None):
    if type:
        type = AnimalTypes.objects.get(id=type)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['farm'] = Farm.objects.get(user = request.user.pk)
        request.POST['type'] = type or request.POST['type']
        form = AnimalForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
        if type:
            return redirect('Farm:Animals:List',type.slug)
        else:
            return redirect('Farm:Animals:List')
    form = AnimalForm({'type':type})
    context = {
        'type' : type ,
        'form' : form ,
    }
    return render(request , 'Animals/Forms/Create.html' , context)

def AddExpence(request , pk):
    animal = Animal.objects.get(pk = pk)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['farm'] = Farm.objects.get(user = request.user.pk)
        request.POST['animal'] = animal
        form = AnimalExpenceForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('Farm:Animals:Detail',pk)
    form = AnimalExpenceForm()
    expence = ([i for i in animal.type.expences.all()])
    context = {
        'form' : form ,
        'expence' : expence ,
        'animal' : animal ,
    }
    return render(request , 'Animals/Forms/AddExpence.html' , context)

def AddProduct(request , pk):
    animal = Animal.objects.get(pk = pk)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['farm'] = Farm.objects.get(user = request.user.pk)
        request.POST['animal'] = animal
        form = AnimalProductForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('Farm:Animals:Detail',pk)
    form = AnimalProductForm()
    product = ([i for i in animal.type.product.all()])
    context = {
        'form' : form ,
        'product' : product ,
        'animal' : animal ,
    }
    return render(request , 'Animals/Forms/AddProduct.html' , context)

def CreateAnimalGroup(request , pk):
    farm = Farm.objects.get(user = request.user.pk)
    type = AnimalTypes.objects.get(pk = pk)
    group_animals = []
    for i in AnimalGroups.objects.filter(farm = farm):
        for v in i.animals.all():
            group_animals.append(v.pk)
    animals = Animal.objects.all().exclude(id__in = group_animals)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['farm'] = Farm.objects.get(user = request.user.pk)
        request.POST['type'] = type
        form = AnimalGroupsForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('Farm:Animals:List')
    form = AnimalGroupsForm()
    context = {
        'form' : form ,
        'type' : type ,
        'animals' : animals ,
    }
    return render(request , 'Animals/Forms/AddAnimalGroup.html' , context)

def AnimalGroup(request , pk):
    group = AnimalGroups.objects.get(pk = pk)
    group_animals = []
    for v in group.animals.all():
        group_animals.append(v.pk)
    animals = Animal.objects.filter(id__in = group_animals)
    context = {
        'group' : group ,
        'animals' : animals ,
    }
    return render(request , 'Animals/Group.html' , context)

def BulkExpence(request , pk):
    group = AnimalGroups.objects.get(pk = pk)
    expences = group.type.expences.all()
    if request.method == 'POST':
        group = AnimalGroups.objects.get(pk = pk)
        group_animals = []
        for v in group.animals.all():
            group_animals.append(v.pk)
        animals = Animal.objects.filter(id__in = group_animals)
        request.POST._mutable = True
        request.POST['farm'] = Farm.objects.get(user = request.user.pk)
        total_qty = request.POST.get('qty')
        for i in animals:
            request.POST['animal'] = i.pk
            request.POST['qty'] = int(total_qty)/len(animals)
            form = AnimalExpenceForm(request.POST)
            if form.is_valid:
                form.save()
        return redirect('Farm:Animals:AnimalGroup',pk)
    form = AnimalExpenceForm()
    context = {
        'form' : form ,
        'group' : group ,
        'expences' : expences ,
    }
    return render(request , 'Animals/Forms/AddBulkExpence.html' , context)
