from django.shortcuts import render, redirect , get_object_or_404 
from .models import Expense,Category
from .forms import Expenseform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ExpenseSerializer
from django.db.models import Sum



# Create your views here.

# View to add an expense

@login_required  # This ensures that the user is logged in

def add_expense(request):
    if request.method == 'POST': # POST meaning the user is submitting the form/data
        form = Expenseform(request.POST)  # creating an instance of expenseform to store data submitted by the user 
        if form.is_valid(): # validation of the form fields
            expense = form.save(commit = False) # data is added to the db BUT NOT committed. As we want to still make some modifications like linking the data to a user
            expense.user = request.user # Link the expense to the current logged in user
            expense.save()
            return redirect('view_expenses') # Redirect to the expense listing page
    else:
        form = Expenseform() # If the request method isnt a POST mthod , we create a new empty form 
        
    return render(request, 'add_expense.html' , {'form' : form})


# @api_view(['POST'])
# def add_expense_api(request):
#     serializer = ExpenseSerializer(data=request.data)
#     if serializer.is_valid():
#           serializer.save(user=request.user)
#           return Response(serializer.data, status=201)
#     return Response(serializer.error, status=400)
     

    
@login_required
def view_expenses(request):
        expenses = Expense.objects.filter(user = request.user)

        search_query = request.GET.get('search','')
        category_filter = request.GET.get('category','')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date:
             expenses = expenses.filter(date__gte=start_date)

        if end_date:
             expenses = expenses.filter(date__lte=end_date)

        if search_query:
             expenses = expenses.filter(title__icontains=search_query)

        if category_filter:
             expenses = expenses.filter(category__name__iexact=category_filter)

        categories = Category.objects.all()
        
        Total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        
        return render(request, 'view_expenses.html', {'expenses' : expenses,
                                                      'categories' :categories,
                                                      'search_query' : search_query,
                                                      'selected_category' : category_filter,
                                                      'total' : Total
        })

from django.db.models import Sum

def home(request):  # adding a view for the home page
    user_expenses = Expense.objects.filter(user=request.user)
    total = user_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    count = user_expenses.count()
    top_cat = user_expenses.values('category__name').annotate(total=Sum('amount')).order_by('-total').first()
    top_category = top_cat['category__name'] if top_cat else "N/A"
    category_data = user_expenses.values('category__name').annotate(total=Sum('amount'))

    chart_labels = [item['category__name'] for item in category_data]
    chart_data = [float(item['total']) for item in category_data]

    # Create a dict for the template legend
    chart_data_dict = {item['category__name']: float(item['total']) for item in category_data}

    return render(request, 'home.html', {
        'total_expenses': total,
        'expense_count': count,
        'top_category': top_category,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'chart_data_dict': chart_data_dict,  # Add this!
    })



def expenses_home(request):
     return render(request,'expenses_home.html')

def signup(request):
    if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login')
    else:
        form = UserCreationForm()

    return render(request , 'signup.html' , {'form':form})

@login_required
def edit_expense(request,id):
    expense = Expense.objects.get(id=id)
     #get the requested expense by id

    if (request.method == "POST"):
          form = Expenseform(request.POST,instance=expense)
          if form.is_valid():
                form.save()
                return redirect('view_expenses')
    else:
          form = Expenseform(instance=expense)
    return render(request, 'edit_expense.html', {'form' : form})

         
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id , user=request.user)

    if(request.method == "POST"):
         expense.delete()
         return redirect('view_expenses')
    
    return render(request, 'delete_expense.html', {'expense':expense})

# @api_view(['DELETE'])
# def delete_expense_api(request,id):
#     try:
#         expense = Expense.objects.get(id=id)
#         expense.delete()
#         return Response({'message':'Expense deleted successfully'},status=204)
#     except Expense.DoesNotExist:
#          return Response({'error':'Expense not found'},status=404)
         
         



