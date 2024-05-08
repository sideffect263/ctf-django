from django.contrib import admin
from .models import Member , LevelsPassed
# Register your models here.
admin.site.register(Member)
admin.site.register(LevelsPassed)
admin.site.index_title="CTF_ZONE"
admin.site.site_header="CTF_ZONE"
admin.site.site_title="CTF_ZONE"




