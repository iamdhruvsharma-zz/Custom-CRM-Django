from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = "__all__" #For all the fields in the Order