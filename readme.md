# Forms in Django
### url routing
```djangourlpath
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('order/', views.order, name='order')
]
```
- when the user visits localhost:8000/order
- Django will look into order function inside views.py

### views.py
```python
def order(request):
    if request.method == 'POST':
        filled_form = IceCreamsForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for ordering ice cream, your %s and %s ice cream is on it's way" %\
                   (filled_form.cleaned_data['flavours'],
                    filled_form.cleaned_data['size'], )
            new_form = IceCreamsForm()
            return render(request, 'icecreams/order.html', {'icecreams_form': new_form, 'note':note})

    else:
        form = IceCreamsForm()
        return render(request, 'icecreams/order.html', {'icecreams_form': form})
```
- if the order function inside view.py checks if the user has pressed the submit button present inside the order.html form tag using the below code
```python
if request.method == 'POST':
    
```
- if the user clicked submit we will clean the data and return the user with a new form for along with information of the order commited.
- views.py
```python
def order(request):
    if request.method == 'POST':
        filled_form = IceCreamsForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for ordering ice cream, your %s and %s ice cream is on it's way" %\
                   (filled_form.cleaned_data['flavours'],
                    filled_form.cleaned_data['size'], )
            new_form = IceCreamsForm()
            return render(request, 'icecreams/order.html', {'icecreams_form': new_form, 'note': note})
```
- we user string string interpolation to display order details to user after he confirms the order
# Models
- models.py
```python
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class IceCream(models.Model):
    flavour1 = models.CharField(max_length=100)
    flavour2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
```
- Data for Class Size is given by us inside admin panel
- we create two classes Size and IceCream
- In IceCream model size is used as a foreign key that links the Class model fields with the Size class
# Forms.py
```python
class IceCreamsForm(forms.ModelForm):

    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = IceCream
        fields = ['flavour1', 'flavour2', 'size']
        labels = {'flavour1': 'Flavour 1', 'flavour2': 'Flavour 2'}
        widgets = {'size': forms.CheckboxSelectMultiple}


# class IceCreamsForm(forms.Form):
#    flavours = forms.MultipleChoiceField(choices=[('choco', 'chocolate'), ('vnl', 'vanilla'),
#                                                  ('butter', 'butterscotch')], widget=forms.CheckboxSelectMultiple)
#    Size = forms.ChoiceField(label='Quantity', choices=[('single scoop', 'single scoop'), ('Double Scoop',
#                                                                                          'Double Scoop'),
#                                                        ('Extra Large Scoop', 'Extra Large Scoop')])
```
- we can further customize forms using labels and widgets as shown above
# Form Template
- order.html
```html
<!DOCTYPE html>
{% load bootstrap4 %}
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<h1>order Ice Cream</h1>
<form action="{% url 'order' %}" method="POST">
	{% csrf_token %}
	{{ icecreams_form }}
	<h2>{{ note }}</h2>
	<input type="submit" value="Order IceCream" class="btn btn-primary">
</form>
```