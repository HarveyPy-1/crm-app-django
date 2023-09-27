from django.db import models

# Any type of database you use will work here with this same code

# Django pluralizes the db name. Leave it as singular
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)

    # Default values to return when you query a user
    def __str__(self):
        return (f"{self.first_name} {self.last_name} {self.email}")
