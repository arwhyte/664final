from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Movie, Director


class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))

class DirectorForm(forms.ModelForm):
	class Meta:
		model = Director
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))