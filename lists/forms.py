from django import forms
from lists.models import Item



EMPTY_LIST_ERROR = '你不能输入一个空的列表值'
class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
            'text': forms.fields.TextInput(attrs={'placeholder': 'Enter a to-do item', 'class': 'form-control input-lg'}),
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }