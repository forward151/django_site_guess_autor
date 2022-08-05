from .models import TaskF, Table, TableAuthors, Test
from django.forms import ModelForm, TextInput, FileInput

#
class TaskFormF(ModelForm):
    class Meta:
        model = TaskF
        fields = ['title', 'task_1']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию автора'
            }),
            'task_1': FileInput(attrs={}),
        }




class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['surname', 'len_of_sentence', 'len_of_words', 'num_of_prep_a', 'num_of_prep_b', 'num_of_prep_c', 'num_of_prep_d', 'num_of_prep_e', 'num_of_prep_f', 'num_of_prep_g', 'num_of_prep_h', 'num_of_prep_i', 'part_of_speech_a', 'part_of_speech_b', 'part_of_speech_c', 'part_of_speech_d', 'part_of_speech_e', 'part_of_speech_f']


class TableAuthorsForm(ModelForm):
    class Meta:
        model = TableAuthors
        fields = ['surname', 'len_of_sentence', 'len_of_words', 'num_of_prep_a', 'num_of_prep_b', 'num_of_prep_c', 'num_of_prep_d', 'num_of_prep_e', 'num_of_prep_f', 'num_of_prep_g', 'num_of_prep_h', 'num_of_prep_i', 'part_of_speech_a', 'part_of_speech_b', 'part_of_speech_c', 'part_of_speech_d', 'part_of_speech_e', 'part_of_speech_f']

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['task']
        widgets = {
            'task': FileInput(attrs={}),
        }
