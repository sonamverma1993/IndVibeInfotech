from django.db import models
#from phonenumber_field.formfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 20)
    # phone = PhoneNumberField(null=False, blank=False, unique=True)
    contact_no = models.CharField(max_length=10)
    subject = models.CharField(max_length = 50)
    message = models.CharField(max_length = 500)

    class Meta:
        db_table = "Contact_Details"