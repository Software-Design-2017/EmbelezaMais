from django.contrib import admin
from user.models import TargetGenre, OperatingHours, Company, PhoneCompany
from user.models import PicturesCompany, User
# Register your models here.
admin.site.register(TargetGenre)
admin.site.register(PicturesCompany)
admin.site.register(OperatingHours)
admin.site.register(Company)
admin.site.register(PhoneCompany)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'password']


admin.site.register(User, UserAdmin)
