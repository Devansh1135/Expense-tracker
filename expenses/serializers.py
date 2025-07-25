from rest_framework import serializers
from .models import Expense, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class ExpenseSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Expense
        fields = '__all__'
