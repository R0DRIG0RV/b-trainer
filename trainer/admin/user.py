from django.contrib import admin

from trainer.models.user import User


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)