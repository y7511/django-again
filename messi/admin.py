from django.contrib import admin
from .models import CompanyInformation, Product, Category , abouttable , contact_admin

admin.site.register(CompanyInformation)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(abouttable)
admin.site.register(contact_admin)
