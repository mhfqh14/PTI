from django.db import models

# Create your models here.

class user(models.Model):
	username = models.CharField(max_length=100, primary_key=True)
	password = models.CharField(max_length=255)
	nama = models.CharField(max_length=255)
	email = models.EmailField()
	alamat = models.TextField()
	nomor_handphone = models.CharField(max_length=16)

	def __str__(self):
		return "{}.{}".format(self.username)

# class editor(models.Model):
# 	username = models.CharField(max_length=100)
# 	password = models.CharField(max_length=255)
# 	nama = models.CharField(max_length=255, primary_key=True)
# 	email = models.EmailField()

# 	def __str__(self):
# 		return "{}.{}".format(self.username)