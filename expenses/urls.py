from django.urls import path
from . import views

urlpatterns = [
    path('',views.expenses_home , name = 'expenses_home'),
    path('add/',views.add_expense, name='add_expense'),
    path('view/', views.view_expenses, name='view_expenses'),
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/',views.delete_expense, name='delete_expense'),
    # path('api/expenses/',views.get_expenses, name = 'get_expenses'),
    # path('api/expense/<int:id>/', views.get_expense,name = 'get_expense' ),
    # path('api/expenses/add/',views.add_expense_api, name = 'add_expense_api'),
    # path('api/expenses/edit/<int:id>', views.edit_expense_api, name = 'edit_expense_api'),
    # path('api/expense/delete/<int:id>',views.delete_expense_api, name='delete_expense_api'),
]