from django.contrib import admin
from .models import *

# Register your models here.


#class HotelAdmin(admin.ModelAdmin):
#    list_display = ['thumbnail', 'name', 'user', 'status']
#    prepopulated_fields = {'slug': ("name", )}


admin.site.register(Booking)

admin.site.register(Hotel)

admin.site.register(HotelGallery)
admin.site.register(HotelFeatures)
admin.site.register(HotelFaqs)
admin.site.register(StaffOnDuty)
admin.site.register(Room)
admin.site.register(RoomType)


#HotelAdmin