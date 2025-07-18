from  django import forms
from .models import Expense , Category

class Expenseform(forms.ModelForm):
    
    # We choose Modelform here as it automatically validates the user input based on the models constraints like required fields , choices etc 

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")

    class Meta:
        model = Expense   # notifying the model we're creating the form for (Expense in this case)

        fields = ['amount' , 'category' , 'description' , 'date','title']

        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
            }
        # Specifying the fields we want the users to fill out
