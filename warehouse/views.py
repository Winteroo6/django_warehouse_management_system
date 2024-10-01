from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

#from .filters import OrderFilter

def registerPage(request):


		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()

				user = form.cleaned_data.get('username')
				messages.success(request, 'Account Has Been Created For ' + user)

				return redirect('login')

		context = {'form': form}		
		return render(request, 'warehouse/register.html', context)

def loginPage(request):
    form = AuthenticationForm()  # Initialize the form

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Bind the POST data to the form

        if form.is_valid():  # Validate the form
            username = form.cleaned_data['username']  # Get the cleaned username
            password = form.cleaned_data['password']  # Get the cleaned password

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to the home page
            else:
                messages.info(request, 'Incorrect Username Or Password')
        else:
            messages.error(request, 'Invalid form submission')

    context = {'form': form}  # Pass the form back to the template
    return render(request, 'warehouse/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	orders = Outbound.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()


	context = {'orders': orders, 'customers':customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}

	return render(request, 'warehouse/dashboard.html', context)

@login_required(login_url='login')
def inventory(request):
	products = Inventory.objects.all()
	return render(request, 'warehouse/inventory.html', {'inventory': products})

@login_required(login_url='login')
def customers(request):
	return render(request, 'warehouse/customers.html')

@login_required(login_url='login')
def createOrder(request):

	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form}
	return render(request, 'warehouse/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

	form = OrderForm()

	context = {'form':form}
	return render(request, 'warehouse/order_form.html', context)		