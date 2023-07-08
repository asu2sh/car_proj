from django.shortcuts import render
from .forms import CustomerForm, CarForm
from .models import Customer, Car, Address

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddressSerializer, CustomerSerializer, CarSerializer


def multi_step_form(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        car_form = CarForm(request.POST)

        if customer_form.is_valid() and car_form.is_valid():
            customer_data = customer_form.cleaned_data
            car_data = car_form.cleaned_data

            address = Address.objects.create(
                street_name=customer_data['address'],
                pincode=customer_data['pincode'],
                city=customer_data['city'],
                state=customer_data['state'],
                country_code=customer_data['country_code']
            )

            customer = Customer.objects.create(
                first_name=customer_data['first_name'],
                last_name=customer_data['last_name'],
                age=customer_data['age'],
                date_of_birth=customer_data['date_of_birth'],
                address=address,
                phone=customer_data['phone'],
                email=customer_data['email']
            )

            car = Car.objects.create(
                model_name=car_data['model_name'],
                manufacturing_date=car_data['manufacturing_date'],
                manufacturer=car_data['manufacturer'],
                color=car_data['color']
            )

            car.save()
            address.save()
            customer.save()

            return render(request, 'done.html')
    else:
        customer_form = CustomerForm()
        car_form = CarForm()

    return render(request, 'form.html', {'customer_form': customer_form, 'car_form': car_form})


class AddressCreateView(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CustomerCreateView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CarCreateView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class AllDataView(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        customers = Customer.objects.all()
        cars = Car.objects.all()

        address_serializer = AddressSerializer(addresses, many=True)
        customer_serializer = CustomerSerializer(customers, many=True)
        car_serializer = CarSerializer(cars, many=True)

        data = {
            'addresses': address_serializer.data,
            'customers': customer_serializer.data,
            'cars': car_serializer.data
        }

        return Response(data)
