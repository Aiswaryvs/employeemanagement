from rest_framework import serializers
from django.contrib.auth.models import User
from employee.models import Employee


class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

    def validate(self, data):
        salary=data.get("salary")
        exp=data.get("experience")
        if salary<0 and exp<0:
            raise serializers.ValidationError("Both salary and Experience are Invalid")
        elif salary<0:
            raise serializers.ValidationError("invalid Salary")
        elif exp<0:
            raise serializers.ValidationError("invalid Experience")
        return data

class EmpRegSeializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
              "username", "email","password"
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)