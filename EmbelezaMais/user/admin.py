from django.contrib import admin

from user.models import TargetGenre, OperatingHours, PhoneCompany, PicturesCompany
from .models import Client, Company


class UserClientAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'phone_number',
                    'is_active',
                    ]


admin.site.register(Client, UserClientAdmin)


class UserCompanyAdmin(admin.ModelAdmin):
    list_display = ['email',
                    'name',
                    'description',
                    'target_genre',
                    'location',
                    'is_active'
                    ]


admin.site.register(Company, UserCompanyAdmin)
admin.site.register(TargetGenre)
admin.site.register(PicturesCompany)
admin.site.register(OperatingHours)
admin.site.register(PhoneCompany)
