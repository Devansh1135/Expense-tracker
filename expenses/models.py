from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.name
    
# Create your models here.
class Expense(models.Model):

    # Defining a list for choices reprensented to the user
    # CATEGORY_CHOICES = [
    #     ('Food','Food'),
    #     ('Transport','Transport'),
    #     ('Entertainment','Entertainment'),
    #     ('Bills','Bills'),
    #     ('Shopping','Shopping'),
    #     ('Other','Other'),
    # ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # if user is deleted , it will delete all the entries (i.e expenses) too

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Store the  amount spent

    # category = models.CharField(max_length=20 , choices=CATEGORY_CHOICES)
    # using the CATEGORY_CHOICES list created earlier to store the selected option in the category field

    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)

    description = models.TextField(blank=True , null=True)
    # Optional field for user to describe the expense

    date = models.DateField()
    # Store date of expense

    title = models.CharField(max_length=250, default="Untitled")

    def __str__(self):
        return f"{self.user.username} - {self.category} - $(self.amount)"
    

    


    