from django.contrib import admin

from asset_management_app.models import Assets, Category, SubCategory, Vendors, Employees, Organization

# Register your models here.

admin.site.register(Assets)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Vendors)
admin.site.register(Employees)
admin.site.register(Organization)
