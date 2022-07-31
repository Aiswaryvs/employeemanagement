from django import forms
class MathForm(forms.Form):
    n1=forms.IntegerField(label="Enter number1")
    n2=forms.IntegerField(label="Enter number2")
    def clean(self):
      cleaned_data= super().clean()
      n1=cleaned_data.get("n1")
      n2=cleaned_data.get("n2")
      if n1<0:
          msg="invalid number"
          self.add_error("n1",msg)
      if n2<0:
          msg="invalid number"
          self.add_error("n2",msg)

class FactForm(forms.Form):
    n1 = forms.IntegerField(label="Enter number")
    def clean(self):
        cleaned_data=super().clean()
        n1=cleaned_data.get("n1")
        if n1<0:
            msg="Invalid number"
            self.add_error("n1",msg)
class EmpForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name "}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}))
    exp=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Experience"}))
    def clean(self):
        cleaned_data=super().clean()
        exp=cleaned_data.get("exp")
        if exp<0:
            msg="invalid Experience"
            self.add_error("exp",msg)
