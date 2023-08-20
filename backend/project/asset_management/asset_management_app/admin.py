from asset_management_app.models import (
    Assets,
    Category,
    Employees,
    Organization,
    SubCategory,
    Vendors,
)
from django.contrib import admin

# Register your models here.

admin.site.register(Assets)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Vendors)
admin.site.register(Employees)
admin.site.register(Organization)
