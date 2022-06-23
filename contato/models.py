from django.db import models



class Contact(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField(error_messages={'required': 'Please enter your email'})
    numero = models.IntegerField()
    message = models.TextField()


    def __str__(self):
        return self.email
