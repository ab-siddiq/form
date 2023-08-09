from django import forms
# widgets == convert field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="Your Name: ",initial="Siddiq",help_text="Enter Full Name",required=False,disabled=True,widget=forms.Textarea(attrs={'id':'name'}))
    email = forms.EmailField()
    file = forms.FileField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    # CHOICES = [('S','Small'),('L','Large'),('M','Medium')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)