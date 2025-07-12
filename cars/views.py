from django.shortcuts import render, redirect
from .models import TBCars

def index(request):
    return render(request, 'cars/index.html', {'appType': 'Django'})

def createcar(request):
    return render(request, 'cars/createcar.html')

def create_car_save(request):
    if request.method == 'POST':
        fName = request.POST['carName']
        fBrand = request.POST['carBrand']
        fModel = request.POST['carModel']
        fPrice = request.POST['carPrice']

        TBCars.objects.create(
            carname=fName,
            carbrand=fBrand,
            carmodel=fModel,
            carprice=fPrice
        )
        return redirect('readcar')

def read_car(request):
    rows = TBCars.objects.all()
    return render(request, 'cars/readcar.html', {'rows': rows, 'appType': 'Django'})

def update_car(request, car_id):
    car = TBCars.objects.get(id=car_id)
    if request.method == 'POST':
        car.carname = request.POST['carName']
        car.carbrand = request.POST['carBrand']
        car.carmodel = request.POST['carModel']
        car.carprice = request.POST['carPrice']
        car.save()
        return redirect('readcar')
    return render(request, 'cars/updatecar.html', {'car': car, 'appType': 'Django'})

def delete_car(request):
    return render(request, 'cars/deletecar.html')

def delete_car_save(request):
    if request.method == 'POST':
        fName = request.POST['carName']
        TBCars.objects.filter(carname=fName).delete()
        return redirect('readcar')

def help_page(request):
    return render(request, 'cars/help.html')

def update_car_input(request):
    context = {'appType': 'Django'}

    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        context['query'] = car_id  # untuk menampilkan input kembali jika tidak ditemukan

        # Validasi ID hanya jika isinya angka
        if car_id and car_id.isdigit():
            if TBCars.objects.filter(id=car_id).exists():
                return redirect('updatecar', car_id=car_id)
            else:
                context['not_found'] = True
        else:
            context['not_found'] = True  # ID tidak valid

    return render(request, 'cars/updatecar_input.html', context)

def search_car(request):
    query = request.GET.get('q')
    if query:
        results = TBCars.objects.filter(
            carname__icontains=query
        ) | TBCars.objects.filter(
            carbrand__icontains=query
        )
    else:
        results = []

    return render(request, 'cars/searchcar.html', {
        'results': results,
        'query': query,
        'appType': 'Django'
    })
