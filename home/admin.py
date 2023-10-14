from django.contrib import admin
from home.models import Contact, cartitem, user,login
from home.models import comments

# Register your models here.
class NameAdmin(admin.ModelAdmin):
    list_display = ('username','password','accountcreated')
admin.site.register(user, NameAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(cartitem)
class cartitemAdmin(admin.ModelAdmin):
    list_display = ('username','item')
    
@admin.register(login)
class loginAdmin(admin.ModelAdmin):
    list_display=('username','lastlogin')
    
@admin.register(comments)
class commentsAdmin(admin.ModelAdmin):
    list_display=('username','commenttime')
    
    


    


