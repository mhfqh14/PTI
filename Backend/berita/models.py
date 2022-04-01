from django.db import models
from home.models import admin

# Create your models here.

class berita(models.Model):
	judul = models.CharField(max_length=200, primary_key=True)
	tanggal = models.DateField()
	penulis= models.CharField(max_length=100)
	editor= models.ForeignKey(admin, on_delete=models.CASCADE)
	gambar= models.ImageField(max_length=255)
	isi_berita= models.TextField()

	def __str__(self):
		return "{}.{}".format(self.judul, self.tanggal)