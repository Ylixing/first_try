from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

# Register your models here.


# admin.site.register(User)

@admin.register(User)
class AuthorizationUserAdmin(admin.ModelAdmin):
    # 不显示open_id
    exclude = ['open_id']
    pass