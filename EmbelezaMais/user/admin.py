from django.contrib import admin
from user.models import TargetGenre, OperatingHours, Company, PhoneCompany
from user.models import PicturesCompany


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'description', 'target_genre', 'location', 'is_active']


admin.site.register(Company, UserAdmin)
admin.site.register(TargetGenre)
admin.site.register(PicturesCompany)
admin.site.register(OperatingHours)
admin.site.register(PhoneCompany)
