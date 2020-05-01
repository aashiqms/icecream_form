from django import forms
from . models import IceCream
from . models import Size


class IceCreamsForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = IceCream
        fields = ['flavour1', 'flavour2', 'size']
        labels = {'flavour1': 'Flavour 1', 'flavour2': 'Flavour 2'}
        widgets = {'size': forms.CheckboxSelectMultiple()}


class NoOfIceCreamsForm(forms.ModelForm):
    number = forms.IntegerField(min_value=2, max_value=30)


# class IceCreamsForm(forms.Form):
#    flavours = forms.MultipleChoiceField(choices=[('choco', 'chocolate'), ('vnl', 'vanilla'),
#                                                  ('butter', 'butterscotch')], widget=forms.CheckboxSelectMultiple)
#    Size = forms.ChoiceField(label='Quantity', choices=[('single scoop', 'single scoop'), ('Double Scoop',
#                                                                                          'Double Scoop'),
#                                                        ('Extra Large Scoop', 'Extra Large Scoop')])

