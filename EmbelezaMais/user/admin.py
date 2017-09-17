from django.contrib import admin
from .models import Client


class UserAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'email',
                    'phone_number',
                    'is_active',
                    ]


admin.site.register(Client, UserAdmin)
