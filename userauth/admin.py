from django.contrib import admin

from .models import userBaseInfo, serverUniversalKey, userTokenInfo

# Register your models here.
admin.site.register(userBaseInfo)
admin.site.register(serverUniversalKey)
admin.site.register(userTokenInfo)