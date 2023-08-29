from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll', 'city']
    
    def get_form(self,request, obj=None, **kwargs):
        form = super().get_form(request,obj,**kwargs)
        is_superuser = request.user.is_superuser

        if is_superuser:
            form.base_fields['name'].disabled = True
        return form