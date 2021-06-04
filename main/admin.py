from django.contrib import admin
from .models import User_info, User_tel,User_law_info,Education_info,User_housemate,User_housemate_tel, Property_info, Property_photo, Tex_info, Room_info, Garden_info, Plant_type_doc, Plant_type_fact, Planting_plan

admin.site.register(User_info)
admin.site.register(User_tel)
admin.site.register(Education_info)
admin.site.register(User_law_info)
admin.site.register(User_housemate)
admin.site.register(User_housemate_tel)
admin.site.register(Property_info)
admin.site.register(Property_photo)
admin.site.register(Tex_info)
admin.site.register(Room_info)
admin.site.register(Garden_info)
admin.site.register(Plant_type_doc)
admin.site.register(Plant_type_fact)
admin.site.register(Planting_plan)

