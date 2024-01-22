from django.db import models
from django_resized import ResizedImageField

class City(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    email = models.EmailField(max_length=100,null=True)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"contact info {self.address}"

    
class HealthFacilityCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HealthFacility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(HealthFacilityCategory, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(Contact, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MedicalSpecialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ResizedImageField(size=[500, 500], upload_to='medical_specialty_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HealthSpecialist(models.Model):
    PROFESSIONAL_TITLES = (
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
        ('DR', 'Dr.'),
        ('PROF', 'Prof.')

    )

    full_name = models.CharField(max_length=50)
    avatar = models.ImageField( upload_to='medical_specialists/', null=True,default='medical_specialists/doctor.png')
    professional_title = models.CharField(max_length=4,choices=PROFESSIONAL_TITLES,default='MR')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    medical_specialty = models.ForeignKey(MedicalSpecialty, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(Contact, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name