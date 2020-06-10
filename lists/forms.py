from django import forms
from lists.models import Item
from django.core.exceptions import ValidationError


DUPLICATE_ITEM_ERROR = "你已经输入过一次了"
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
    def save(self, for_list):
        self.instance.list = for_list
        return super().save()

class ExistingListItemForm(ItemForm):
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):
        return forms.models.ModelForm.save(self)