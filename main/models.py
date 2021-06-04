from django.db import models


class User_info(models.Model):
    full_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='avatars/')
    birth_date = models.CharField(max_length=12)
    sex = models.CharField(max_length=10)
    passport_data = models.CharField(max_length=9)
    inn = models.CharField(max_length=10)
    home_tel = models.CharField(max_length=13, default=None, null=True)
    family = models.CharField(max_length=10)
    actual_address = models.CharField(max_length=50, default=None)
    registration_address = models.CharField(max_length=50)
    work_info = models.CharField(max_length=50)
    education = models.CharField(max_length=50, blank=True, null=True)
    law_status = models.BooleanField()

    def __str__(self):
        return self.full_name


# номер пользователя
class User_tel(models.Model):
    User_tel = models.ForeignKey(User_info, on_delete=models.CASCADE)
    phone_tel = models.CharField(max_length=13)

    def __str__(self):
        return self.User_tel.full_name


# информация об образовании
class Education_info(models.Model):
    education_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    start_date = models.CharField(max_length=12)
    finish_date = models.CharField(max_length=12)

    def __str__(self):
        name_split=self.education_info.full_name.split(' ')
        return f'{name_split[0]}  {self.education_info.passport_data}'


# информаци о судимости
class User_law_info(models.Model):
    User_law_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
    law_num = models.CharField(max_length=50)
    date = models.CharField(max_length=12)


# информаци о сожителе
class User_housemate(models.Model):
    User_housemate = models.ForeignKey(User_info, on_delete=models.CASCADE)
    housemate_name = models.CharField(max_length=50)


# номер пользователя
class User_housemate_tel(models.Model):
    User_housemate_tel = models.ForeignKey(User_housemate, on_delete=models.CASCADE)
    phone_tel = models.CharField(max_length=13)


# информация об имуществе
class Property_info(models.Model):
    Property_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
    adress = models.CharField(max_length=50)
    kadastr_number = models.CharField(max_length=20)
    kadastr_sum = models.CharField(max_length=20)
    economic_num = models.CharField(max_length=20)
    floor = models.CharField(max_length=2)
    total_area = models.CharField(max_length=50)
    house_area = models.CharField(max_length=50)
    living_room = models.CharField(max_length=50)
    extra_info = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    register_number = models.CharField(max_length=50)
    register_date = models.CharField(max_length=12)
    foundation_documents = models.FileField()
    kadastr_copy = models.FileField(upload_to='files/')
    kadastr_contract_number = models.CharField(max_length=50)
    kadastr_contract_date = models.CharField(max_length=12)
    # garden_area = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Property_info.full_name}  {self.kadastr_number}'


# фотографии имущества
class Property_photo(models.Model):
    Property_photo = models.ForeignKey(Property_info, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='property_photos/')

    def __str__(self):
        # name_split=self.Property_photo.Property_info.full_name.split(' ')
        return f'{self.Property_photo}  '


#
class Tex_info(models.Model):
    Tex_info = models.ForeignKey(Property_info, on_delete=models.CASCADE)
    build_date = models.CharField(max_length=12)
    floor_count = models.CharField(max_length=50)
    wall_material = models.CharField(max_length=50)
    electricity = models.BooleanField()
    gas = models.BooleanField()
    water = models.BooleanField()
    heating = models.BooleanField()
    water_2 = models.BooleanField()
    communication = models.BooleanField()
    lift = models.BooleanField()

    def __str__(self):
        return f'Техническая информация  {self.Tex_info.kadastr_number}  '

#
class Room_info(models.Model):
    Room_info = models.ForeignKey(Property_info, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    room_area = models.CharField(max_length=50)


#
class Garden_info(models.Model):
    Garden_info = models.ForeignKey(User_info, on_delete=models.CASCADE)
    area = models.CharField(max_length=50)


#
class Plant_type_doc(models.Model):
    Plant_type_doc = models.ForeignKey(Garden_info, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


#
class Plant_type_fact(models.Model):
    Plant_type_fact = models.ForeignKey(Garden_info, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


#
class Planting_plan(models.Model):
    Planting_plan = models.ForeignKey(Garden_info, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    count = models.CharField(max_length=50)
