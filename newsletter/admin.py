from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

# Register your models here.
class SingUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "update",]
    form = SignUpForm
    #class Meta:
    #    model = SignUp

admin.site.register(SignUp, SingUpAdmin)